# tests/test_integration.py
"""
Integration tests for the Multi-Agent Legal Assistant.
These tests verify that components work together correctly.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()


class TestVectorDBIntegration:
    """Integration tests for Vector Database."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        self.persist_dir = os.getenv("PERSIST_DIRECTORY_PATH", "./vectordb")
        self.collection_name = os.getenv("IPC_COLLECTION_NAME", "ipc_collection")
    
    def test_vectordb_exists(self):
        """Vector database directory should exist."""
        assert os.path.exists(self.persist_dir)
    
    def test_vectordb_has_data(self):
        """Vector database should have IPC data."""
        from langchain_chroma import Chroma
        from langchain_huggingface import HuggingFaceEmbeddings
        
        embeddings = HuggingFaceEmbeddings()
        db = Chroma(
            collection_name=self.collection_name,
            persist_directory=self.persist_dir,
            embedding_function=embeddings
        )
        
        # Should have documents
        collection = db.get()
        assert len(collection['ids']) > 0
    
    def test_vectordb_search(self):
        """Vector database should return search results."""
        from tools.ipc_sections_search_tool import search_ipc_sections
        
        results = search_ipc_sections.func("theft robbery")
        assert len(results) > 0
        assert "section" in results[0]


class TestAgentsIntegration:
    """Integration tests for CrewAI Agents."""
    
    def test_all_agents_loadable(self):
        """All agents should be importable."""
        from agents.case_intake_agent import case_intake_agent
        from agents.ipc_section_agent import ipc_section_agent
        from agents.legal_precedent_agent import legal_precedent_agent
        from agents.legal_drafter_agent import legal_drafter_agent
        from agents.document_validator_agent import document_validator_agent
        from agents.document_analyzer_agent import document_analyzer_agent
        from agents.document_drafter_agent import document_drafter_agent
        from agents.document_formatter_agent import document_formatter_agent
        
        assert case_intake_agent is not None
        assert ipc_section_agent is not None
        assert legal_precedent_agent is not None
        assert legal_drafter_agent is not None
        assert document_validator_agent is not None
        assert document_analyzer_agent is not None
        assert document_drafter_agent is not None
        assert document_formatter_agent is not None


class TestCrewsIntegration:
    """Integration tests for CrewAI Crews."""
    
    def test_legal_assistant_crew_loadable(self):
        """Legal assistant crew should be importable."""
        from crew import legal_assistant_crew
        assert legal_assistant_crew is not None
    
    def test_document_crew_loadable(self):
        """Document drafting crew should be importable."""
        from document_crew import document_drafting_crew
        assert document_drafting_crew is not None


class TestTemplatesAndPDFIntegration:
    """Integration tests for Templates and PDF generation."""
    
    def test_template_to_pdf(self):
        """Should generate PDF from template."""
        from templates.legal_templates import RentalAgreementTemplate
        from tools.pdf_generator import PDFGenerator
        
        # Generate template content
        data = {
            "landlord_name": "Test Landlord",
            "tenant_name": "Test Tenant",
            "property_address": "123 Test Street",
            "rent_amount": "25000",
            "security_deposit": "50000",
            "agreement_duration": "11 months"
        }
        template = RentalAgreementTemplate(data)
        content = template.generate()
        
        # Generate PDF
        generator = PDFGenerator()
        result = generator.generate_pdf(
            content=content,
            filename="test_integration",
            title="Rental Agreement",
            return_bytes=True
        )
        
        assert result["status"] == "success"
        assert result["data"].startswith(b'%PDF')
    
    def test_registry_to_pdf(self):
        """Should generate PDF using registry."""
        from templates.base_template import TemplateRegistry
        from tools.pdf_generator import DocumentExporter
        
        # Get template from registry
        template = TemplateRegistry.get_template("affidavit", {
            "deponent_name": "Test Person",
            "deponent_address": "Test Address",
            "purpose": "Test Purpose"
        })
        
        assert template is not None
        
        # Generate content
        content = template.generate()
        assert len(content) > 100
        
        # Export
        exporter = DocumentExporter()
        pdf_bytes = exporter.get_pdf_bytes(content, "Affidavit")
        assert pdf_bytes is not None


class TestValidatorsIntegration:
    """Integration tests for Validators with real inputs."""
    
    def test_criminal_case_validation(self):
        """Should validate and classify criminal case."""
        from utils.validators import validate_legal_query
        
        query = """
        My neighbor has been threatening me with violence for the past 3 months.
        Yesterday he attacked me with a wooden stick causing injuries.
        He has also been extorting money from local shopkeepers.
        I want to file a complaint under appropriate IPC sections.
        """
        
        result = validate_legal_query(query)
        assert result.is_valid
        assert result.extracted_info.get("detected_domain") == "criminal"
    
    def test_document_request_validation(self):
        """Should validate and classify document request."""
        from utils.validators import validate_document_request
        
        request = """
        I need a rental agreement for my 2BHK apartment in Bangalore.
        Landlord: Suresh Kumar, Address: MG Road, Bangalore
        Tenant: Ramesh Singh, rent: Rs. 30,000 per month
        Security deposit: Rs. 1,00,000, Duration: 11 months
        Starting from: 1st February 2024
        """
        
        result = validate_document_request(request)
        assert result.is_valid
        assert result.extracted_info.get("detected_document_type") == "rental_agreement"


class TestLoggingIntegration:
    """Integration tests for logging system."""
    
    def test_logger_works(self):
        """Logger should work correctly."""
        from utils.logger import get_logger
        
        logger = get_logger("test_logger")
        logger.info("Test info message")
        logger.debug("Test debug message")
        logger.warning("Test warning message")
        
        # Should not raise any errors
        assert True
    
    def test_agent_action_logging(self):
        """Should log agent actions."""
        from utils.logger import get_logger
        
        logger = get_logger("agent_test")
        logger.log_agent_action(
            agent_name="Case Intake Agent",
            action="Processing query",
            details="Criminal case about theft"
        )
        
        # Should not raise any errors
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
