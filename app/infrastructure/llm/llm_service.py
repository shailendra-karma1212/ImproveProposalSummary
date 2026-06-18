import os

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from app.infrastructure.prompt.prompt import (
    get_summary_improvement_prompt
)

load_dotenv()


class LLMService:

    def __init__(self):

        self.llm = ChatMistralAI(
            model="mistral-large-latest",
            api_key=os.getenv(
                "MISTRAL_API_KEY"
            ),
            temperature=0
        )

    def generate_improved_summary(
        self,
        chunk_text: str,
        previous_summary: str,
        user_instruction: str
    ):

        prompt = (
            get_summary_improvement_prompt(
                chunk_text=chunk_text,
                previous_summary=previous_summary,
                user_instruction=user_instruction
            )
        )

        response = self.llm.invoke(
            prompt
        )

        return response.content
    
#-------------------------
#log
from app.utility.log import setup_logger

logger = setup_logger(__name__)
def generate_improved_summary(
    self,
    chunk_text,
    previous_summary,
    user_instruction
):

    try:

        logger.info(
            "Sending request to LLM"
        )

        response = self.llm.invoke(
            prompt
        )

        logger.info(
            "Summary generated successfully"
        )

        return response.content

    except Exception as e:

        logger.error(
            f"LLM Error: {str(e)}"
        )

        raise