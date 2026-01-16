# document_validator_agent.py

from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# Use CrewAI's native LLM format for Groq
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)

document_validator_agent = Agent(
    role="Legal Document Request Validator",
    goal=(
        "Validate whether the user's request is legal-related and identify any missing "
        "critical information such as names, dates, locations, document type, or parties involved. "
        "Ask clarifying questions only for genuinely missing information."
    ),
    backstory=(
        "You are an experienced legal intake officer with expertise in analyzing document requests. "
        "You are skilled at determining what information is essential for legal document drafting "
        "and identifying gaps that must be filled before proceeding. You ask precise, non-repetitive "
        "questions and clearly explain why each piece of information is needed."
    ),
    tools=[],
    llm=llm,
    verbose=True,
)
