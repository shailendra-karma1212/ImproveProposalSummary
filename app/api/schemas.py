from pydantic import BaseModel


class ImproveSummaryRequest(BaseModel):
    companyId: str
    tenderId: str
    documentId: str
    RelatedSection: str
    previousSummary: str
    instruction: str


class ImproveSummaryResponse(BaseModel):
    success: bool
    source_chunk: str
    improved_summary: str