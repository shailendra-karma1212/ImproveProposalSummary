import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.infrastructure.log.agent_logger import AgentLogger


from app.infrastructure.prompt.prompt import get_summary_improvement_prompt

from app.utility.log import setup_logger

load_dotenv()

logger = setup_logger(__name__)


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=os.getenv(
                "LLM_MODEL",
                "gpt-4.1"
            ),
            temperature=0,
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def generate_improved_summary(
        self,
        chunk_text: str,
        section_name: str,
        previous_summary: str,
        instruction: str
    ):

        try:

            logger.info(
                "Sending request to LLM"
            )

            prompt = get_summary_improvement_prompt(
                chunk_text=chunk_text,
                section_name=section_name,
                previous_summary=previous_summary,
                instruction=instruction
            )

            response = self.llm.invoke(prompt)

            logger.info(
                "Summary generated successfully"
            )

            return response.content

        except Exception as e:

            logger.error(
                f"LLM Error: {str(e)}"
            )

            raise


#-----------------------------------------------------------------
#log


agent_logger = AgentLogger()
agent_logger.log_event(
    agent_name="SummaryImprovementAgent",
    message="Sending request to LLM",
    event_type="LLM_REQUEST",
    source_module="llm_service.py",
    is_success=True
)
