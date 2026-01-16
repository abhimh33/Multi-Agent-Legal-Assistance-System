# document_crew.py

from crewai import Crew
from dotenv import load_dotenv
import os

# Load environment variables first
load_dotenv()

# Disable OpenAI fallback
os.environ["OPENAI_API_KEY"] = ""

from agents.document_validator_agent import document_validator_agent
from agents.document_analyzer_agent import document_analyzer_agent
from agents.document_drafter_agent import document_drafter_agent
from agents.document_formatter_agent import document_formatter_agent
from tasks.document_validator_task import document_validator_task
from tasks.document_analyzer_task import document_analyzer_task
from tasks.document_drafter_task import document_drafter_task
from tasks.document_formatter_task import document_formatter_task

document_drafting_crew = Crew(
    agents=[
        document_validator_agent,
        document_analyzer_agent,
        document_drafter_agent,
        document_formatter_agent
    ],
    tasks=[
        document_validator_task,
        document_analyzer_task,
        document_drafter_task,
        document_formatter_task
    ],
    verbose=True,
    memory=False  # Disabled - uses OpenAI embeddings by default
)
