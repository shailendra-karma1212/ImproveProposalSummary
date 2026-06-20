from fastapi import (
    APIRouter,
    HTTPException
)
from app.infrastructure.log.agent_logger import AgentLogger
from app.api.schemas import ImproveSummaryRequest,ImproveSummaryResponse


from app.services.qudrant.qudrant_service import QdrantService


from app.infrastructure.llm.llm_service import LLMService

router = APIRouter()

qdrant_service = QdrantService()
llm_service = LLMService()


@router.post(
    "/improve-summary",
    response_model=ImproveSummaryResponse
)
async def improve_summary(
    payload: ImproveSummaryRequest
):

    try:
        chunk_text = qdrant_service.fetch_combined_chunk(
            company_id=payload.companyId,
            tender_id=payload.tenderId,
            document_id=payload.documentId,
        )



        if not chunk_text:

            raise HTTPException(
                status_code=404,
                detail="Chunk not found"
            )

        improved_summary = llm_service.generate_improved_summary(
            chunk_text=chunk_text,
            section_name=payload.sectionName,
            previous_summary=payload.previousSummary,
            instruction=payload.instruction,
        )


        return ImproveSummaryResponse(
            success=True,
            source_chunk=chunk_text,
            improved_summary=improved_summary
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    

#-------------------------------------------------
#loog
from app.infrastructure.log.agent_logger import AgentLogger


agent_logger = AgentLogger()
agent_logger.log_event(
    agent_name="SummaryImprovementAgent",
    message="Request received",
    event_type="REQUEST_RECEIVED",
    source_module="routes.py",
    is_success=True
)