# document_formatter_agent.py

from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# Use CrewAI's native LLM format for Groq
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)

document_formatter_agent = Agent(
    role="Legal Document Formatter and Reviewer",
    goal=(
        "Format the drafted legal document for professional presentation and printing. "
        "Ensure proper headings, numbered clauses, clean spacing, consistent formatting, "
        "and a layout suitable for standard paper size. Review the document for completeness "
        "and clarity before final delivery."
    ),
    backstory=(
        "You are a detail-oriented legal document formatter with expertise in creating "
        "professional, printable legal documents. You ensure that all documents meet "
        "professional standards for formatting, spacing, numbering, and presentation. "
        "You catch any inconsistencies or formatting issues and ensure the final document "
        "looks polished and professional."
    ),
    tools=[],
    llm=llm,
    verbose=True,
)
