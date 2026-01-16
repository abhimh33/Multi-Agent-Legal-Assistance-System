# document_drafter_task.py

from crewai import Task
from agents.document_drafter_agent import document_drafter_agent

document_drafter_task = Task(
    description=(
        "Draft a professional legal document based on the analysis: {user_input}\n\n"
        "Analysis provided:\n"
        "{analysis_result}\n\n"
        "Your task is to:\n"
        "1. Create a complete legal document using formal legal language\n"
        "2. Follow the proposed structure from the analysis\n"
        "3. Include all necessary clauses and provisions\n"
        "4. Ensure the document is neutral and balanced\n"
        "5. Make the document immediately actionable and complete\n"
        "6. Do not add unnecessary explanations or assumptions\n"
        "7. Use standard legal document formatting conventions\n\n"
        "The draft should include:\n"
        "- Proper heading and title\n"
        "- All parties clearly identified\n"
        "- Date and location information\n"
        "- Numbered clauses and sections\n"
        "- All terms, conditions, and obligations\n"
        "- Signature blocks and witness lines (if applicable)\n"
        "- Any required legal disclaimers or notices"
    ),
    expected_output=(
        "A complete, professionally drafted legal document in formal legal language, "
        "ready for review and use. The document should be comprehensive and require "
        "only minor adjustments before finalization."
    ),
    agent=document_drafter_agent,
)
