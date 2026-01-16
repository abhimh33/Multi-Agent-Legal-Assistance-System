# tests/test_templates.py
"""
Unit tests for document templates.
"""

import pytest
import sys
import os
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from templates.base_template import DocumentTemplate, TemplateRegistry, DocumentSection
from templates.legal_templates import (
    RentalAgreementTemplate,
    AffidavitTemplate,
    LegalNoticeTemplate,
    PowerOfAttorneyTemplate,
    ContractTemplate,
    NDAAgreementTemplate,
    EmploymentAgreementTemplate
)


class TestTemplateRegistry:
    """Tests for TemplateRegistry class."""
    
    def test_list_templates_not_empty(self):
        """Registry should have registered templates."""
        templates = TemplateRegistry.list_templates()
        assert len(templates) > 0
    
    def test_get_rental_template(self):
        """Should retrieve rental agreement template."""
        template = TemplateRegistry.get_template("rental_agreement")
        assert template is not None
        assert isinstance(template, RentalAgreementTemplate)
    
    def test_get_nda_template(self):
        """Should retrieve NDA template."""
        template = TemplateRegistry.get_template("nda")
        assert template is not None
        assert isinstance(template, NDAAgreementTemplate)
    
    def test_get_nonexistent_template(self):
        """Should return None for nonexistent template."""
        template = TemplateRegistry.get_template("nonexistent_template")
        assert template is None
    
    def test_template_info(self):
        """Should get template info."""
        info = TemplateRegistry.get_template_info()
        assert len(info) > 0
        assert all("name" in t for t in info)
        assert all("display_name" in t for t in info)


class TestRentalAgreementTemplate:
    """Tests for RentalAgreementTemplate."""
    
    def test_generate_with_data(self):
        """Should generate document with provided data."""
        data = {
            "landlord_name": "John Doe",
            "tenant_name": "Jane Smith",
            "property_address": "123 Main Street, Delhi",
            "rent_amount": "25000",
            "security_deposit": "50000",
            "agreement_duration": "11 months"
        }
        template = RentalAgreementTemplate(data)
        result = template.generate()
        
        assert "John Doe" in result
        assert "Jane Smith" in result
        assert "123 Main Street" in result
        assert "25000" in result
        assert "11 months" in result
    
    def test_generate_without_data(self):
        """Should generate document with placeholders when no data."""
        template = RentalAgreementTemplate()
        result = template.generate()
        
        assert "[LANDLORD NAME]" in result
        assert "[TENANT NAME]" in result
    
    def test_structure_defined(self):
        """Should have defined structure."""
        template = RentalAgreementTemplate()
        structure = template.get_structure()
        
        assert len(structure) > 0
        assert any(s["section"] == "parties" for s in structure)
        assert any(s["section"] == "rent" for s in structure)
    
    def test_required_fields_defined(self):
        """Should have required fields defined."""
        template = RentalAgreementTemplate()
        assert "landlord_name" in template.required_fields
        assert "tenant_name" in template.required_fields
        assert "rent_amount" in template.required_fields


class TestAffidavitTemplate:
    """Tests for AffidavitTemplate."""
    
    def test_generate_with_data(self):
        """Should generate affidavit with provided data."""
        data = {
            "deponent_name": "Ram Kumar",
            "deponent_address": "456 MG Road, Mumbai",
            "deponent_age": "45",
            "deponent_occupation": "Business",
            "purpose": "Address Proof",
            "statements": ["I reside at the above address", "This is my permanent residence"]
        }
        template = AffidavitTemplate(data)
        result = template.generate()
        
        assert "Ram Kumar" in result
        assert "456 MG Road" in result
        assert "45" in result
        assert "Address Proof" in result
        assert "VERIFICATION" in result
    
    def test_statements_as_list(self):
        """Should handle statements as list."""
        data = {
            "deponent_name": "Test Person",
            "deponent_address": "Test Address",
            "purpose": "Test Purpose",
            "statements": ["Statement 1", "Statement 2", "Statement 3"]
        }
        template = AffidavitTemplate(data)
        result = template.generate()
        
        assert "1." in result
        assert "2." in result


class TestLegalNoticeTemplate:
    """Tests for LegalNoticeTemplate."""
    
    def test_generate_legal_notice(self):
        """Should generate legal notice."""
        data = {
            "sender_name": "ABC Company",
            "sender_address": "Corporate Office, Delhi",
            "recipient_name": "XYZ Ltd",
            "recipient_address": "Business Park, Mumbai",
            "subject": "Breach of Contract",
            "facts": "You have failed to deliver goods as per contract dated 01/01/2024",
            "demand": "Deliver the goods within 7 days or pay damages of Rs. 5,00,000"
        }
        template = LegalNoticeTemplate(data)
        result = template.generate()
        
        assert "LEGAL NOTICE" in result
        assert "ABC Company" in result
        assert "XYZ Ltd" in result
        assert "Breach of Contract" in result


class TestPowerOfAttorneyTemplate:
    """Tests for PowerOfAttorneyTemplate."""
    
    def test_generate_poa(self):
        """Should generate power of attorney."""
        data = {
            "principal_name": "Senior Citizen",
            "principal_address": "Pune",
            "attorney_name": "Son's Name",
            "attorney_address": "Delhi",
            "poa_type": "General",
            "powers": "To manage all my bank accounts and property matters"
        }
        template = PowerOfAttorneyTemplate(data)
        result = template.generate()
        
        assert "POWER OF ATTORNEY" in result
        assert "Senior Citizen" in result
        assert "Son's Name" in result
        assert "PRINCIPAL" in result
        assert "ATTORNEY" in result


class TestContractTemplate:
    """Tests for ContractTemplate."""
    
    def test_generate_contract(self):
        """Should generate contract agreement."""
        data = {
            "party_a_name": "Company A",
            "party_b_name": "Company B",
            "contract_purpose": "Software development services"
        }
        template = ContractTemplate(data)
        result = template.generate()
        
        assert "CONTRACT AGREEMENT" in result
        assert "Company A" in result
        assert "Company B" in result


class TestNDATemplate:
    """Tests for NDAAgreementTemplate."""
    
    def test_generate_nda(self):
        """Should generate NDA."""
        data = {
            "disclosing_party": "Tech Startup",
            "receiving_party": "Investor Group",
            "purpose": "Investment discussions"
        }
        template = NDAAgreementTemplate(data)
        result = template.generate()
        
        assert "NON-DISCLOSURE" in result
        assert "CONFIDENTIAL" in result.upper()
        assert "Tech Startup" in result


class TestEmploymentAgreementTemplate:
    """Tests for EmploymentAgreementTemplate."""
    
    def test_generate_employment_agreement(self):
        """Should generate employment agreement."""
        data = {
            "employer_name": "Tech Corp Ltd",
            "employee_name": "New Employee",
            "designation": "Software Engineer",
            "salary": "80000"
        }
        template = EmploymentAgreementTemplate(data)
        result = template.generate()
        
        assert "EMPLOYMENT AGREEMENT" in result
        assert "Tech Corp Ltd" in result
        assert "Software Engineer" in result
        assert "80000" in result


class TestDocumentSection:
    """Tests for DocumentSection dataclass."""
    
    def test_to_text_simple(self):
        """Should convert simple section to text."""
        section = DocumentSection(
            title="Test Section",
            content="Test content here",
            section_number="1"
        )
        result = section.to_text()
        
        assert "1. Test Section" in result
        assert "Test content" in result
    
    def test_to_text_with_subsections(self):
        """Should handle subsections."""
        subsection = DocumentSection(
            title="Subsection",
            content="Sub content",
            section_number="1.1"
        )
        section = DocumentSection(
            title="Main Section",
            content="Main content",
            section_number="1",
            subsections=[subsection]
        )
        result = section.to_text()
        
        assert "Main Section" in result
        assert "Subsection" in result


class TestNumberToWords:
    """Tests for number to words conversion."""
    
    def test_small_numbers(self):
        """Should convert small numbers correctly."""
        template = RentalAgreementTemplate()
        assert template._number_to_words(5) == "Five"
        assert template._number_to_words(15) == "Fifteen"
        assert template._number_to_words(99) == "Ninety Nine"
    
    def test_thousands(self):
        """Should convert thousands correctly."""
        template = RentalAgreementTemplate()
        result = template._number_to_words(25000)
        assert "Thousand" in result
    
    def test_lakhs(self):
        """Should convert lakhs correctly (Indian system)."""
        template = RentalAgreementTemplate()
        result = template._number_to_words(500000)
        assert "Lakh" in result
    
    def test_crores(self):
        """Should convert crores correctly (Indian system)."""
        template = RentalAgreementTemplate()
        result = template._number_to_words(10000000)
        assert "Crore" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
