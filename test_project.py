# test_project.py
"""
Quick System Health Check for the Multi-Agent Legal Assistant.
Run this script to verify all components are working correctly.
"""

import sys
import os
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

def print_header(text):
    """Print a formatted header."""
    print(f"\n{'='*60}")
    print(f" {text}")
    print(f"{'='*60}")

def print_status(name, status, message=""):
    """Print a status line."""
    icon = "✅" if status else "❌"
    msg = f" - {message}" if message else ""
    print(f"   {icon} {name}{msg}")

def check_environment():
    """Check environment variables."""
    print_header("1. ENVIRONMENT VARIABLES")
    
    required_vars = [
        ("GROQ_API_KEY", "LLM Provider"),
        ("TAVILY_API_KEY", "Precedent Search"),
        ("PERSIST_DIRECTORY_PATH", "Vector DB Path"),
        ("IPC_COLLECTION_NAME", "IPC Collection")
    ]
    
    all_ok = True
    for var, desc in required_vars:
        value = os.getenv(var)
        if value:
            masked = value[:8] + "..." if len(value) > 10 else value
            print_status(f"{var} ({desc})", True, f"Set: {masked}")
        else:
            print_status(f"{var} ({desc})", False, "NOT SET")
            all_ok = False
    
    return all_ok

def check_vectordb():
    """Check vector database."""
    print_header("2. VECTOR DATABASE")
    
    try:
        persist_dir = os.getenv("PERSIST_DIRECTORY_PATH", "./vectordb")
        
        if os.path.exists(persist_dir):
            print_status("Vector DB directory exists", True, persist_dir)
        else:
            print_status("Vector DB directory", False, "Not found")
            return False
        
        # Check SQLite file
        sqlite_path = os.path.join(persist_dir, "chroma.sqlite3")
        if os.path.exists(sqlite_path):
            size_mb = os.path.getsize(sqlite_path) / (1024 * 1024)
            print_status("ChromaDB SQLite file", True, f"{size_mb:.2f} MB")
        else:
            print_status("ChromaDB SQLite file", False, "Not found")
            return False
        
        # Try loading the database
        from langchain_chroma import Chroma
        from langchain_huggingface import HuggingFaceEmbeddings
        
        embeddings = HuggingFaceEmbeddings()
        collection_name = os.getenv("IPC_COLLECTION_NAME", "ipc_collection")
        
        db = Chroma(
            collection_name=collection_name,
            persist_directory=persist_dir,
            embedding_function=embeddings
        )
        
        collection = db.get()
        doc_count = len(collection['ids'])
        print_status(f"IPC Collection loaded", True, f"{doc_count} documents")
        
        return True
        
    except Exception as e:
        print_status("Vector database check", False, str(e))
        return False

def check_agents():
    """Check CrewAI agents."""
    print_header("3. CREWAI AGENTS")
    
    agents_to_check = [
        ("agents.case_intake_agent", "case_intake_agent", "Case Intake Agent"),
        ("agents.ipc_section_agent", "ipc_section_agent", "IPC Section Agent"),
        ("agents.legal_precedent_agent", "legal_precedent_agent", "Legal Precedent Agent"),
        ("agents.legal_drafter_agent", "legal_drafter_agent", "Legal Drafter Agent"),
        ("agents.document_validator_agent", "document_validator_agent", "Document Validator Agent"),
        ("agents.document_analyzer_agent", "document_analyzer_agent", "Document Analyzer Agent"),
        ("agents.document_drafter_agent", "document_drafter_agent", "Document Drafter Agent"),
        ("agents.document_formatter_agent", "document_formatter_agent", "Document Formatter Agent"),
    ]
    
    all_ok = True
    for module, attr, name in agents_to_check:
        try:
            mod = __import__(module, fromlist=[attr])
            agent = getattr(mod, attr)
            print_status(name, True, f"Role: {agent.role[:40]}...")
        except Exception as e:
            print_status(name, False, str(e)[:50])
            all_ok = False
    
    return all_ok

def check_crews():
    """Check CrewAI crews."""
    print_header("4. CREWAI CREWS")
    
    try:
        from crew import legal_assistant_crew
        print_status("Legal Assistant Crew", True, f"{len(legal_assistant_crew.agents)} agents")
    except Exception as e:
        print_status("Legal Assistant Crew", False, str(e)[:50])
        return False
    
    try:
        from document_crew import document_drafting_crew
        print_status("Document Drafting Crew", True, f"{len(document_drafting_crew.agents)} agents")
    except Exception as e:
        print_status("Document Drafting Crew", False, str(e)[:50])
        return False
    
    return True

def check_tools():
    """Check CrewAI tools."""
    print_header("5. CREWAI TOOLS")
    
    try:
        from tools.ipc_sections_search_tool import search_ipc_sections
        result = search_ipc_sections.func("theft")
        print_status("IPC Search Tool", True, f"Found {len(result)} results for 'theft'")
    except Exception as e:
        print_status("IPC Search Tool", False, str(e)[:50])
    
    try:
        from tools.legal_precedent_search_tool import search_legal_precedents
        print_status("Legal Precedent Tool", True, "Loaded (requires API call)")
    except Exception as e:
        print_status("Legal Precedent Tool", False, str(e)[:50])
    
    try:
        from tools.document_export_tool import export_document, preview_document
        print_status("Document Export Tool", True, "Loaded")
    except Exception as e:
        print_status("Document Export Tool", False, str(e)[:50])
    
    try:
        from tools.pdf_generator import PDFGenerator, DocumentExporter
        print_status("PDF Generator", True, "Loaded")
    except Exception as e:
        print_status("PDF Generator", False, str(e)[:50])
    
    return True

def check_templates():
    """Check document templates."""
    print_header("6. DOCUMENT TEMPLATES")
    
    try:
        from templates.base_template import TemplateRegistry
        templates = TemplateRegistry.list_templates()
        print_status("Template Registry", True, f"{len(templates)} templates registered")
        
        # List templates
        print("\n   Available Templates:")
        for t in sorted(set(templates)):
            print(f"      - {t}")
        
        # Test one template
        template = TemplateRegistry.get_template("rental_agreement", {
            "landlord_name": "Test Landlord",
            "tenant_name": "Test Tenant"
        })
        if template:
            content = template.generate()
            print_status("Template Generation", True, f"Generated {len(content)} characters")
        
    except Exception as e:
        print_status("Templates", False, str(e)[:50])
        return False
    
    return True

def check_utils():
    """Check utility modules."""
    print_header("7. UTILITY MODULES")
    
    # Logger
    try:
        from utils.logger import get_logger
        logger = get_logger("test")
        logger.info("Test log message")
        print_status("Logger", True, "Working")
    except Exception as e:
        print_status("Logger", False, str(e)[:50])
    
    # Validators
    try:
        from utils.validators import validate_legal_query, validate_document_request
        
        result = validate_legal_query("A theft occurred at my house last night and valuables were stolen")
        print_status("Legal Query Validator", True, f"Valid: {result.is_valid}")
        
        result = validate_document_request("I need a rental agreement for my property in Delhi with rent of Rs. 25000")
        print_status("Document Request Validator", True, f"Type: {result.extracted_info.get('detected_document_type', 'N/A')}")
    except Exception as e:
        print_status("Validators", False, str(e)[:50])
    
    # Exceptions
    try:
        from utils.exceptions import LegalAssistantError, ValidationError
        print_status("Custom Exceptions", True, "Loaded")
    except Exception as e:
        print_status("Custom Exceptions", False, str(e)[:50])
    
    return True

def run_quick_integration_test():
    """Run a quick integration test."""
    print_header("8. QUICK INTEGRATION TEST")
    
    try:
        # Test PDF generation
        from tools.pdf_generator import PDFGenerator
        generator = PDFGenerator()
        
        result = generator.generate_pdf(
            content="Test legal document content.\n\nSection 1: Introduction\n\nThis is a test.",
            filename="test_integration",
            title="Integration Test",
            return_bytes=True
        )
        
        if result["status"] == "success":
            print_status("PDF Generation", True, f"Generated {len(result['data'])} bytes")
        else:
            print_status("PDF Generation", False, result.get("message", "Unknown error"))
        
        # Test template + PDF
        from templates.base_template import TemplateRegistry
        template = TemplateRegistry.get_template("affidavit", {
            "deponent_name": "Test Person",
            "deponent_address": "Test Address",
            "purpose": "Testing"
        })
        
        content = template.generate()
        result = generator.generate_pdf(content, return_bytes=True)
        
        if result["status"] == "success":
            print_status("Template to PDF", True, "Working")
        else:
            print_status("Template to PDF", False, result.get("message"))
        
    except Exception as e:
        print_status("Integration Test", False, str(e)[:50])
        return False
    
    return True

def main():
    """Run all system checks."""
    print("\n" + "=" * 60)
    print(" 🏛️  MULTI-AGENT LEGAL ASSISTANT - SYSTEM CHECK")
    print(" " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    
    results = []
    
    results.append(("Environment", check_environment()))
    results.append(("Vector DB", check_vectordb()))
    results.append(("Agents", check_agents()))
    results.append(("Crews", check_crews()))
    results.append(("Tools", check_tools()))
    results.append(("Templates", check_templates()))
    results.append(("Utilities", check_utils()))
    results.append(("Integration", run_quick_integration_test()))
    
    # Summary
    print_header("SUMMARY")
    
    passed = sum(1 for _, status in results if status)
    total = len(results)
    
    for name, status in results:
        print_status(name, status)
    
    print(f"\n   Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 ALL SYSTEMS OPERATIONAL!")
        print("\n   Start the application with:")
        print("   streamlit run app_enhanced.py")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
print("\n2️⃣  LEGAL DOCUMENT CREATION:")
print("   python draft_document.py (CLI mode)")
print("   streamlit run app.py    (Web UI - Create Legal Document tab)")
print("\n3️⃣  TEST VECTOR DATABASE:")
print("   python query_vectordb.py (Check IPC sections)")
