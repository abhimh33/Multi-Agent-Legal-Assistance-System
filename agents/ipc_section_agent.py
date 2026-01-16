# ipc_section_agent.py

from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools.ipc_sections_search_tool import search_ipc_sections

load_dotenv()

# Use CrewAI's native LLM format for Groq
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

ipc_section_agent = Agent(
    role="IPC Section Agent",
    goal="Identify the most relevant Indian Penal Code (IPC) sections based on the legal issue provided.",
    backstory=(
        "You're a seasoned legal researcher with deep knowledge of Indian penal laws. "
        "You specialize in mapping legal issues to applicable IPC sections with precision and clarity. "
        "Your insight helps lawyers and assistants quickly understand the statutory basis of a case."
    ),
    tools=[search_ipc_sections],
    llm=llm,
    verbose=True,
)
