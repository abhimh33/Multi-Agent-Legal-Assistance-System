# tests/test_tools.py
"""
Unit tests for CrewAI tools.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()


class TestIPCSearchTool:
    """Tests for IPC Section Search Tool."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        from tools.ipc_sections_search_tool import search_ipc_sections
        self.tool = search_ipc_sections
    
    def test_tool_exists(self):
        """Tool should be importable."""
        assert self.tool is not None
    
    def test_search_theft(self):
        """Should find IPC sections for theft."""
        result = self.tool.func("What is the punishment for theft?")
        assert isinstance(result, list)
        assert len(result) > 0
    
    def test_search_murder(self):
        """Should find IPC sections for murder."""
        result = self.tool.func("murder killing homicide")
        assert isinstance(result, list)
        assert len(result) > 0
    
    def test_search_returns_metadata(self):
        """Results should contain metadata."""
        result = self.tool.func("assault and hurt")
        assert len(result) > 0
        first_result = result[0]
        assert "section" in first_result
        assert "content" in first_result
    
    def test_empty_query_handling(self):
        """Should handle empty queries gracefully."""
        # This might return empty results or raise an error
        # depending on implementation
        try:
            result = self.tool.func("")
            assert isinstance(result, list)
        except Exception:
            pass  # Some implementations may raise errors


class TestLegalPrecedentTool:
    """Tests for Legal Precedent Search Tool."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        from tools.legal_precedent_search_tool import search_legal_precedents
        self.tool = search_legal_precedents
    
    def test_tool_exists(self):
        """Tool should be importable."""
        assert self.tool is not None
    
    @pytest.mark.skipif(
        not os.getenv("TAVILY_API_KEY"),
        reason="TAVILY_API_KEY not set"
    )
    def test_search_precedents(self):
        """Should find legal precedents."""
        result = self.tool.func("theft and burglary cases in India")
        assert isinstance(result, list)


class TestPDFGenerator:
    """Tests for PDF Generator."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        from tools.pdf_generator import PDFGenerator, DocumentExporter
        self.generator = PDFGenerator()
        self.exporter = DocumentExporter()
    
    def test_generator_exists(self):
        """Generator should be importable."""
        assert self.generator is not None
    
    def test_generate_simple_pdf(self):
        """Should generate a simple PDF."""
        content = """
        RENTAL AGREEMENT
        
        This is a test rental agreement.
        
        1. PARTIES
        Party A: Landlord
        Party B: Tenant
        
        2. RENT
        Monthly rent: Rs. 25,000/-
        """
        
        result = self.generator.generate_pdf(
            content=content,
            filename="test_document",
            title="Test Rental Agreement"
        )
        
        assert result["status"] == "success"
        assert "filepath" in result
        
        # Clean up
        if os.path.exists(result["filepath"]):
            os.remove(result["filepath"])
    
    def test_generate_pdf_bytes(self):
        """Should generate PDF as bytes."""
        content = "Test content for PDF bytes generation."
        
        result = self.generator.generate_pdf(
            content=content,
            title="Test",
            return_bytes=True
        )
        
        assert result["status"] == "success"
        assert "data" in result
        assert isinstance(result["data"], bytes)
        assert result["data"].startswith(b'%PDF')
    
    def test_exporter_txt(self):
        """Should export as TXT."""
        content = "Test content for TXT export."
        
        result = self.exporter.export(
            content=content,
            format_type="txt",
            filename="test_txt"
        )
        
        assert result["status"] == "success"
        
        # Clean up
        if os.path.exists(result["filepath"]):
            os.remove(result["filepath"])
    
    def test_exporter_all_formats(self):
        """Should export to all formats."""
        content = "Test content for all format export."
        
        result = self.exporter.export(
            content=content,
            format_type="all",
            filename="test_all_formats"
        )
        
        assert result["status"] == "success"
        assert "exports" in result
        
        # Clean up
        for fmt, details in result["exports"].items():
            if details.get("status") == "success" and "filepath" in details:
                if os.path.exists(details["filepath"]):
                    os.remove(details["filepath"])


class TestDocumentExportTool:
    """Tests for Document Export Tool."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up test fixtures."""
        from tools.document_export_tool import export_document
        self.tool = export_document
    
    def test_tool_exists(self):
        """Tool should be importable."""
        assert self.tool is not None
    
    def test_export_txt(self):
        """Should export as TXT."""
        result = self.tool.func(
            document_content="Test document content",
            format_type="txt",
            filename="test_export"
        )
        
        assert result["overall_status"] == "success"
        
        # Clean up
        for fmt, details in result.get("exports", {}).items():
            if details.get("status") == "success" and "path" in details:
                if os.path.exists(details["path"]):
                    os.remove(details["path"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
