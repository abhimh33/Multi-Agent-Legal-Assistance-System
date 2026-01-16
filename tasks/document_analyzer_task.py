# document_analyzer_task.py

from crewai import Task
from agents.document_analyzer_agent import document_analyzer_agent

document_analyzer_task = Task(
    description=(
        "Analyze the validated legal document request: {user_input}\n\n"
        "The request has been validated and contains the following information:\n"
        "{validation_result}\n\n"
        "Your task is to:\n"
        "1. Identify the specific document type (contract, agreement, notice, affidavit, etc.)\n"
        "2. Determine the applicable jurisdiction and laws\n"
        "3. Identify all parties involved and their roles\n"
        "4. List the key terms, conditions, and obligations\n"
        "5. Identify any special legal requirements or clauses needed\n"
        "6. Outline the document structure that will be used\n\n"
        "Output format:\n"
        "- DOCUMENT_TYPE: [Type]\n"
        "- JURISDICTION: [Jurisdiction]\n"
        "- PARTIES: [List of parties and roles]\n"
        "- KEY_TERMS: [Key terms and conditions]\n"
        "- LEGAL_REQUIREMENTS: [Applicable laws and requirements]\n"
        "- DOCUMENT_STRUCTURE: [Proposed structure with sections]"
    ),
    expected_output=(
        "A comprehensive analysis of the document requirements including document type, "
        "jurisdiction, parties, key terms, applicable laws, and proposed structure."
    ),
    agent=document_analyzer_agent,
)
