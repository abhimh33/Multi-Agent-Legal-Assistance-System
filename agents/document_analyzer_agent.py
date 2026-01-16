# document_analyzer_agent.py

from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# Use CrewAI's native LLM format for Groq
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

document_analyzer_agent = Agent(
    role="Legal Document Type Analyzer",
    goal=(
        "Analyze the user's document request to identify the specific document type, "
        "jurisdiction, parties involved, key terms, and legal purpose. Provide a structured "
        "analysis that will guide the document drafting process."
    ),
    backstory=(
        "You are an expert legal analyst with deep knowledge of various document types including "
        "contracts, agreements, notices, complaints, affidavits, wills, powers of attorney, and more. "
        "You understand jurisdictional requirements and can identify which laws and regulations apply. "
        "You provide clear, structured analysis that highlights key legal requirements for the document."
    ),
    tools=[],
    llm=llm,
    verbose=True,
)
