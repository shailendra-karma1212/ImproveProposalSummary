import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models

load_dotenv()


class QdrantService:

    def __init__(self):

        # self.client = QdrantClient(
        #     url=os.getenv("QDRANT_URL"),
        #     api_key=os.getenv("QDRANT_API_KEY")
        # )

        self.client = QdrantClient(
    url=os.getenv("QDRANT_URL")
)

        self.collection_name = os.getenv(
            "COLLECTION_NAME"
        )

    def fetch_exact_chunk(
        self,
        company_id: str,
        tender_id: str,
        document_id: str,
        RelatedSection: str
    ):

        result, _ = self.client.scroll(
            collection_name=self.collection_name,

            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="CompanyId",
                        match=models.MatchValue(
                            value=company_id
                        )
                    ),

                    models.FieldCondition(
                        key="TenderId",
                        match=models.MatchValue(
                            value=tender_id
                        )
                    ),

                    models.FieldCondition(
                        key="DocumentId",
                        match=models.MatchValue(
                            value=document_id
                        )
                    ),

                    models.FieldCondition(
                        key="RelatedSection",
                        match=models.MatchValue(
                            value=RelatedSection
                        )
                    )
                ]
            ),

            limit=1,
            with_payload=True,
            with_vectors=False
        )

        if not result:
            return None

        payload = result[0].payload

        if not payload:
            return None

        return payload.get("Text")
    
#------------------------------------------------------------
#log
from app.utility.log import setup_logger

logger = setup_logger(__name__)
def fetch_exact_chunk(
    self,
    company_id,
    tender_id,
    document_id
):

    logger.info(
        f"Searching chunk | CompanyId={company_id} | TenderId={tender_id} | DocumentId={document_id}"
    )

    try:

        result, _ = self.client.scroll(
            ...
        )

        if not result:
            logger.warning("Chunk not found")
            return None

        logger.info("Chunk found successfully")

        return result[0].payload.get("Text")

    except Exception as e:

        logger.error(
            f"Qdrant Error: {str(e)}"
        )

        raise
