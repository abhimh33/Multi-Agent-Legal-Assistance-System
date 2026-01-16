# draft_document.py
"""
Dedicated script for creating legal documents via CLI
"""

from dotenv import load_dotenv
from document_crew import document_drafting_crew

load_dotenv()

def draft_document(document_request: str):
    """
    Main function to process document drafting request
    """
    print("\n" + "="*70)
    print("⚖️  LEGAL DOCUMENT GENERATOR")
    print("="*70 + "\n")
    
    print("📋 Processing your request...\n")
    
    result = document_drafting_crew.kickoff(inputs={
        "user_input": document_request,
        "validation_result": "",
        "analysis_result": "",
        "draft_result": ""
    })
    
    print("\n" + "="*70)
    print("📄 FINAL LEGAL DOCUMENT")
    print("="*70 + "\n")
    print(result)
    print("\n" + "="*70)
    
    # Save to file
    from datetime import datetime
    import os
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exports_dir = os.path.join(os.path.dirname(__file__), "exports")
    os.makedirs(exports_dir, exist_ok=True)
    
    output_file = os.path.join(exports_dir, f"legal_document_{timestamp}.txt")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(result))
    
    print(f"\n✅ Document saved to: {output_file}")
    print("\n💡 Tip: You can open this file in Word/Google Docs for formatting and export to PDF")
    
    return result

if __name__ == "__main__":
    # Example document request
    document_request = """
    I need a rental agreement for my apartment in Mumbai. 
    Owner: Ms. Priya Singh
    Tenant: Mr. Raj Kumar Patel
    Property: 2-BHK apartment, 5th floor, at Mumbai Central
    Rent: 35,000 per month
    Deposit: 3 months (105,000)
    Duration: 2 years starting from February 1, 2024
    Utilities: Tenant responsible for electricity, water, and internet
    Pet policy: No pets allowed
    """
    
    print("Enter document request (or press Enter to use example):")
    user_input = input().strip()
    
    if not user_input:
        user_input = document_request
    
    draft_document(user_input)
