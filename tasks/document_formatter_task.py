# document_formatter_task.py

from crewai import Task
from agents.document_formatter_agent import document_formatter_agent

document_formatter_task = Task(
    description=(
        "Format and review the drafted legal document for final delivery: {user_input}\n\n"
        "Draft provided:\n"
        "{draft_result}\n\n"
        "Your task is to:\n"
        "1. Ensure all headings are properly formatted and consistent\n"
        "2. Verify all clauses are numbered sequentially\n"
        "3. Check spacing and line breaks for professional appearance\n"
        "4. Ensure the document fits standard paper size (A4/Letter)\n"
        "5. Review for any typos, grammatical errors, or inconsistencies\n"
        "6. Verify all required sections are present\n"
        "7. Check that names, dates, and details are consistent throughout\n"
        "8. Ensure proper indentation and alignment\n"
        "9. Add page breaks if necessary\n"
        "10. Provide a final formatted, ready-to-print version\n\n"
        "Output should include:\n"
        "- The fully formatted document\n"
        "- A quality checklist confirming all formatting standards are met\n"
        "- Any recommendations for the user\n"
        "- Instructions for printing or saving to PDF"
    ),
    expected_output=(
        "A professionally formatted legal document that is ready for printing, "
        "PDF conversion, or direct use. Include a quality checklist and "
        "any final recommendations or notes for the user."
    ),
    agent=document_formatter_agent,
)
