# tests/test_exceptions.py
"""
Unit tests for custom exceptions.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.exceptions import (
    LegalAssistantError,
    ValidationError,
    APIError,
    DatabaseError,
    DocumentGenerationError,
    ToolExecutionError,
    ConfigurationError,
    RateLimitError
)


class TestLegalAssistantError:
    """Tests for base LegalAssistantError."""
    
    def test_basic_error(self):
        """Should create basic error."""
        error = LegalAssistantError("Test error")
        assert str(error) == "[UNKNOWN_ERROR] Test error"
    
    def test_error_with_code(self):
        """Should create error with custom code."""
        error = LegalAssistantError("Test error", error_code="TEST_001")
        assert error.error_code == "TEST_001"
    
    def test_error_with_details(self):
        """Should create error with details."""
        error = LegalAssistantError(
            "Test error",
            details={"key": "value"}
        )
        assert error.details["key"] == "value"
    
    def test_to_dict(self):
        """Should convert to dictionary."""
        error = LegalAssistantError(
            "Test error",
            error_code="TEST",
            details={"info": "data"}
        )
        result = error.to_dict()
        
        assert result["error_type"] == "LegalAssistantError"
        assert result["error_code"] == "TEST"
        assert result["message"] == "Test error"


class TestValidationError:
    """Tests for ValidationError."""
    
    def test_validation_error_basic(self):
        """Should create validation error."""
        error = ValidationError("Invalid input")
        assert error.error_code == "VALIDATION_ERROR"
    
    def test_validation_error_with_field(self):
        """Should include field information."""
        error = ValidationError(
            "Field is required",
            field="email"
        )
        assert error.field == "email"
        assert "email" in error.details.get("field", "")
    
    def test_validation_error_with_value(self):
        """Should include invalid value."""
        error = ValidationError(
            "Invalid value",
            invalid_value="bad_data"
        )
        assert error.invalid_value == "bad_data"


class TestAPIError:
    """Tests for APIError."""
    
    def test_api_error_basic(self):
        """Should create API error."""
        error = APIError("API failed", api_name="Groq")
        assert error.error_code == "API_ERROR"
        assert error.api_name == "Groq"
    
    def test_api_error_with_status(self):
        """Should include status code."""
        error = APIError(
            "Server error",
            api_name="Tavily",
            status_code=500
        )
        assert error.status_code == 500
        assert error.details["status_code"] == 500


class TestDatabaseError:
    """Tests for DatabaseError."""
    
    def test_database_error(self):
        """Should create database error."""
        error = DatabaseError("Connection failed", database_type="chroma")
        assert error.error_code == "DATABASE_ERROR"
        assert error.database_type == "chroma"


class TestDocumentGenerationError:
    """Tests for DocumentGenerationError."""
    
    def test_document_error(self):
        """Should create document generation error."""
        error = DocumentGenerationError(
            "PDF generation failed",
            document_type="rental_agreement",
            stage="formatting"
        )
        assert error.error_code == "DOCUMENT_GENERATION_ERROR"
        assert error.document_type == "rental_agreement"
        assert error.stage == "formatting"


class TestToolExecutionError:
    """Tests for ToolExecutionError."""
    
    def test_tool_error(self):
        """Should create tool execution error."""
        error = ToolExecutionError(
            "Tool failed",
            tool_name="search_ipc_sections"
        )
        assert error.error_code == "TOOL_EXECUTION_ERROR"
        assert error.tool_name == "search_ipc_sections"


class TestConfigurationError:
    """Tests for ConfigurationError."""
    
    def test_config_error(self):
        """Should create configuration error."""
        error = ConfigurationError(
            "API key missing",
            config_key="GROQ_API_KEY"
        )
        assert error.error_code == "CONFIGURATION_ERROR"
        assert error.config_key == "GROQ_API_KEY"


class TestRateLimitError:
    """Tests for RateLimitError."""
    
    def test_rate_limit_error(self):
        """Should create rate limit error."""
        error = RateLimitError(
            "Rate limit exceeded",
            api_name="Groq",
            retry_after=60
        )
        assert error.error_code == "RATE_LIMIT_ERROR"
        assert error.retry_after == 60
        assert error.status_code == 429


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
