import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models

from app.utility.log import setup_logger
from app.infrastructure.log.agent_logger import AgentLogger

load_dotenv()

logger = setup_logger("name")


class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            # api_key=os.getenv("QDRANT_API_KEY"),
            check_compatibility=False,
        )

        self.chunk_collection = os.getenv("CHUNK_COLLECTION")
        self.company_collection = os.getenv("COMPANY_COLLECTION")

    def _scroll_all_texts(self, *, collection_name: str, scroll_filter: models.Filter) -> list[str]:
        """Fetch ALL matching payloads text from Qdrant."""

        texts: list[str] = []
        next_offset = None

        while True:
            result, next_offset = self.client.scroll(
                collection_name=collection_name,
                scroll_filter=scroll_filter,
                limit=100,
                offset=next_offset,
                with_payload=True,
                with_vectors=False,
            )

            for point in result:
                if point.payload:
                    txt = point.payload.get("Text", "")
                    if txt:
                        texts.append(txt)

            if not next_offset:
                break

        return texts

    def fetch_company_chunks(self, company_id: str) -> list[str]:
        logger.info(f"Searching company chunks | CompanyId={company_id}")

        scroll_filter = models.Filter(
            must=[
                models.FieldCondition(
                    key="CompanyId",
                    match=models.MatchValue(value=company_id),
                )
            ]
        )

        texts = self._scroll_all_texts(
            collection_name=self.company_collection,
            scroll_filter=scroll_filter,
        )

        if not texts:
            logger.warning("Company chunks not found")
        else:
            logger.info(f"Company chunks found successfully | count={len(texts)}")

        return texts

    def fetch_tender_chunks(
        self,
        company_id: str,
        tender_id: str,
        # document_id: str,
    ) -> list[str]:
        logger.info(
            "Searching tender chunks | "
            f"CompanyId={company_id} | "
            f"TenderId={tender_id} | "
            # f"DocumentId={document_id}"
        )

        scroll_filter = models.Filter(
            must=[
                models.FieldCondition(
                    key="CompanyId",
                    match=models.MatchValue(value=company_id),
                ),
                models.FieldCondition(
                    key="TenderId",
                    match=models.MatchValue(value=tender_id),
                ),
                # models.FieldCondition(
                #     key="DocumentId",
                #     match=models.MatchValue(value=document_id),
                # ),
            ]
        )

        texts = self._scroll_all_texts(
            collection_name=self.chunk_collection,
            scroll_filter=scroll_filter,
        )

        if not texts:
            logger.warning("Tender chunks not found")
        else:
            logger.info(f"Tender chunks found successfully | count={len(texts)}")

        return texts

    def fetch_combined_chunk(
        self,
        company_id: str,
        tender_id: str,
        # document_id: str,
    ) -> str:
        company_chunks = self.fetch_company_chunks(company_id=company_id)
        tender_chunks = self.fetch_tender_chunks(
            company_id=company_id,
            tender_id=tender_id,
            # document_id=document_id,
        )

        if not company_chunks:
            logger.warning("Company chunks are empty")
        if not tender_chunks:
            logger.warning("Tender chunks are empty")

        company_context = "\n\n".join(company_chunks)
        tender_context = "\n\n".join(tender_chunks)

        combined_chunk = f"""

COMPANY CONTEXT:

{company_context}

==================================================

TENDER CONTEXT:

{tender_context}
"""

        logger.info(f"Combined Chunk Length: {len(combined_chunk)}")
        logger.info("Combined chunk created successfully")

        return combined_chunk



#---------------------------------------------------
#log

agent_logger = AgentLogger()
agent_logger.log_event(
    agent_name="SummaryImprovementAgent",
    message="Company chunk found",
    event_type="FETCH_COMPANY_CHUNK",
    source_module="qudrant_service.py",
    is_success=True,
    payload={
        
    }
)