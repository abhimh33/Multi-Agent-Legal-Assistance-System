# case_intake_agent.py

from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# Use CrewAI's native LLM format for Groq
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

case_intake_agent = Agent(
    role="Case Intake Agent",
    goal=(
        "Understand the user's legal issue and classify it into a"
         " structured format for further legal processing."
    ),
    backstory=(
        "You're a highly skilled legal intake assistant trained to analyze"
        " plain-English legal concerns. "
        "You identify the type of legal issue, categorize it under a domain of law,"
        " and extract relevant context "
        "to pass along to legal researchers, drafters, or compliance teams."
    ),
    llm=llm,
    tools=[],
    verbose=True,
)

