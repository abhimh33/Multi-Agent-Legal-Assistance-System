# document_validator_task.py

from crewai import Task
from agents.document_validator_agent import document_validator_agent

document_validator_task = Task(
    description=(
        "Validate the user's legal document request: {user_input}\n\n"
        "Your task is to:\n"
        "1. Determine if the request is genuinely legal-related\n"
        "2. Identify what type of document is being requested\n"
        "3. Check if all critical information is provided (names, dates, locations, parties, purpose)\n"
        "4. If information is missing, clearly list what additional details are needed\n"
        "5. If the request is complete, confirm it and provide a brief summary\n\n"
        "Output format:\n"
        "- VALIDITY: [Valid/Invalid with reason]\n"
        "- COMPLETENESS: [Complete/Incomplete]\n"
        "- MISSING_INFO: [List of missing details, or 'None']\n"
        "- QUESTIONS: [Specific clarifying questions needed, or 'None']\n"
        "- SUMMARY: [Brief summary of the request]"
    ),
    expected_output=(
        "A clear validation report indicating whether the request is valid, complete, "
        "what information is missing (if any), and what clarifying questions need to be asked."
    ),
    agent=document_validator_agent,
)
