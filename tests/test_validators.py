# tests/test_validators.py
"""
Unit tests for input validation module.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validators import (
    InputValidator,
    ValidationResult,
    validate_legal_query,
    validate_document_request,
    sanitize_input,
    LegalDomain,
    DocumentType
)


class TestInputValidator:
    """Tests for InputValidator class."""
    
    # === Legal Query Validation Tests ===
    
    def test_empty_query_fails(self):
        """Empty queries should fail validation."""
        result = validate_legal_query("")
        assert not result.is_valid
        assert "empty" in result.message.lower()
    
    def test_none_query_fails(self):
        """None queries should fail validation."""
        result = validate_legal_query(None)
        assert not result.is_valid
    
    def test_short_query_fails(self):
        """Queries shorter than minimum length should fail."""
        result = validate_legal_query("theft case")
        assert not result.is_valid
        assert "short" in result.message.lower()
    
    def test_valid_query_passes(self):
        """Valid queries should pass validation."""
        query = """A man broke into my house at night while my family was sleeping. 
        He stole jewelry and cash from our bedroom. When I confronted him, 
        he threatened me with a knife and ran away."""
        result = validate_legal_query(query)
        assert result.is_valid
        assert result.sanitized_input is not None
    
    def test_criminal_domain_detection(self):
        """Criminal keywords should be detected."""
        query = """Someone committed theft and robbery at my shop. 
        The accused also assaulted my employee during the crime."""
        result = validate_legal_query(query)
        assert result.is_valid
        assert result.extracted_info.get("detected_domain") == LegalDomain.CRIMINAL.value
    
    def test_harmful_content_blocked(self):
        """Queries with harmful content should be blocked."""
        query = "This is a legal query <script>alert('xss')</script> about theft"
        result = validate_legal_query(query)
        # Should either sanitize or block
        if result.is_valid:
            assert "<script>" not in result.sanitized_input
    
    def test_excessive_whitespace_normalized(self):
        """Excessive whitespace should be normalized."""
        query = """This    is a    legal query   about   property   dispute   
        with    multiple     spaces    and    line    breaks."""
        result = validate_legal_query(query)
        if result.is_valid:
            assert "    " not in result.sanitized_input
    
    # === Document Request Validation Tests ===
    
    def test_empty_document_request_fails(self):
        """Empty document requests should fail."""
        result = validate_document_request("")
        assert not result.is_valid
    
    def test_short_document_request_fails(self):
        """Short document requests should fail."""
        result = validate_document_request("rental agreement")
        assert not result.is_valid
    
    def test_valid_rental_request_detected(self):
        """Rental agreement requests should be detected."""
        request = """I need a rental agreement for my property located in 
        Delhi. The tenant name is Raj Kumar, rent is Rs. 25000 per month, 
        security deposit is Rs. 50000, and the duration is 11 months."""
        result = validate_document_request(request)
        assert result.is_valid
        assert result.extracted_info.get("detected_document_type") == DocumentType.RENTAL_AGREEMENT.value
    
    def test_nda_request_detected(self):
        """NDA requests should be detected."""
        request = """I need a non-disclosure agreement for my startup. 
        We are sharing confidential business information with a potential 
        investor and need to protect our trade secrets and proprietary data."""
        result = validate_document_request(request)
        assert result.is_valid
        assert result.extracted_info.get("detected_document_type") == DocumentType.NDA.value
    
    def test_employment_request_detected(self):
        """Employment agreement requests should be detected."""
        request = """I need an employment agreement for a new employee joining 
        as Software Engineer. Salary is Rs. 80000 per month, joining date is 
        February 1, 2024, probation period is 6 months."""
        result = validate_document_request(request)
        assert result.is_valid
        assert result.extracted_info.get("detected_document_type") == DocumentType.EMPLOYMENT_AGREEMENT.value
    
    def test_date_extraction(self):
        """Dates should be extracted from requests."""
        request = """I need a rental agreement starting from 15/03/2024. 
        The property will be rented for 11 months ending on 14/02/2025."""
        result = validate_document_request(request)
        assert result.is_valid
        assert "dates" in result.extracted_info.get("entities", {})
    
    def test_amount_extraction(self):
        """Amounts should be extracted from requests."""
        request = """I need a sale deed for property worth Rs. 50,00,000. 
        The token amount paid is ₹5,00,000 and remaining amount is Rs. 45 lakhs."""
        result = validate_document_request(request)
        assert result.is_valid
        assert "amounts" in result.extracted_info.get("entities", {})
    
    # === Sanitization Tests ===
    
    def test_sanitize_removes_scripts(self):
        """Sanitization should remove script tags."""
        text = "Hello <script>evil()</script> World"
        result = sanitize_input(text)
        assert "<script>" not in result
        assert "</script>" not in result
    
    def test_sanitize_removes_null_bytes(self):
        """Sanitization should remove null bytes."""
        text = "Hello\x00World"
        result = sanitize_input(text)
        assert "\x00" not in result
    
    def test_sanitize_preserves_valid_content(self):
        """Sanitization should preserve valid content."""
        text = "This is a valid legal query about property dispute."
        result = sanitize_input(text)
        assert "valid legal query" in result


class TestValidationResult:
    """Tests for ValidationResult dataclass."""
    
    def test_bool_conversion_valid(self):
        """Valid results should be truthy."""
        result = ValidationResult(is_valid=True, message="OK")
        assert bool(result) is True
    
    def test_bool_conversion_invalid(self):
        """Invalid results should be falsy."""
        result = ValidationResult(is_valid=False, message="Failed")
        assert bool(result) is False
    
    def test_warnings_default_empty(self):
        """Warnings should default to empty list."""
        result = ValidationResult(is_valid=True, message="OK")
        assert result.warnings == []
    
    def test_extracted_info_default_empty(self):
        """Extracted info should default to empty dict."""
        result = ValidationResult(is_valid=True, message="OK")
        assert result.extracted_info == {}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
