# utils/validators.py
"""
Input Validation Module for the Multi-Agent Legal Assistant.
Provides comprehensive validation for user inputs and document requests.
"""

import re
from typing import Optional, List, Tuple, Dict, Any
from dataclasses import dataclass, field
from enum import Enum


class LegalDomain(Enum):
    """Supported legal domains."""
    CRIMINAL = "criminal"
    CIVIL = "civil"
    CORPORATE = "corporate"
    FAMILY = "family"
    LABOR = "labor"
    PROPERTY = "property"
    CONSUMER = "consumer"
    CONSTITUTIONAL = "constitutional"
    TAX = "tax"
    GENERAL = "general"


class DocumentType(Enum):
    """Supported legal document types."""
    RENTAL_AGREEMENT = "rental_agreement"
    SALE_DEED = "sale_deed"
    POWER_OF_ATTORNEY = "power_of_attorney"
    AFFIDAVIT = "affidavit"
    LEGAL_NOTICE = "legal_notice"
    CONTRACT = "contract"
    WILL = "will"
    PARTNERSHIP_DEED = "partnership_deed"
    MOU = "memorandum_of_understanding"
    NDA = "non_disclosure_agreement"
    EMPLOYMENT_AGREEMENT = "employment_agreement"
    COMPLAINT = "complaint"
    REPLY = "reply"
    GENERAL = "general"


@dataclass
class ValidationResult:
    """Result of a validation operation."""
    is_valid: bool
    message: str
    warnings: List[str] = field(default_factory=list)
    sanitized_input: Optional[str] = None
    extracted_info: Dict[str, Any] = field(default_factory=dict)
    
    def __bool__(self) -> bool:
        return self.is_valid


class InputValidator:
    """Comprehensive input validation for legal queries and document requests."""
    
    # Minimum and maximum lengths for inputs
    MIN_QUERY_LENGTH = 20
    MAX_QUERY_LENGTH = 10000
    MIN_DOCUMENT_REQUEST_LENGTH = 30
    MAX_DOCUMENT_REQUEST_LENGTH = 15000
    
    # Potentially harmful patterns to filter
    HARMFUL_PATTERNS = [
        r'<script.*?>.*?</script>',  # Script tags
        r'javascript:',  # JavaScript URLs
        r'on\w+\s*=',  # Event handlers
        r'<iframe.*?>',  # iFrames
        r'<object.*?>',  # Object tags
    ]
    
    # Legal document keywords for detection
    DOCUMENT_KEYWORDS = {
        DocumentType.RENTAL_AGREEMENT: ["rent", "rental", "lease", "tenant", "landlord", "tenancy"],
        DocumentType.SALE_DEED: ["sale", "sell", "purchase", "buyer", "seller", "property sale"],
        DocumentType.POWER_OF_ATTORNEY: ["power of attorney", "poa", "authorize", "attorney"],
        DocumentType.AFFIDAVIT: ["affidavit", "sworn statement", "declare", "oath"],
        DocumentType.LEGAL_NOTICE: ["legal notice", "notice", "demand", "warning"],
        DocumentType.CONTRACT: ["contract", "agreement", "terms", "conditions"],
        DocumentType.WILL: ["will", "testament", "inheritance", "bequest", "heir"],
        DocumentType.PARTNERSHIP_DEED: ["partnership", "partner", "partners deed"],
        DocumentType.MOU: ["mou", "memorandum", "understanding"],
        DocumentType.NDA: ["nda", "non-disclosure", "confidentiality", "confidential"],
        DocumentType.EMPLOYMENT_AGREEMENT: ["employment", "employee", "job", "salary", "work agreement"],
    }
    
    # Criminal law keywords
    CRIMINAL_KEYWORDS = [
        "theft", "murder", "assault", "robbery", "fraud", "cheating",
        "criminal", "crime", "offense", "offence", "ipc", "fir", "police",
        "arrest", "bail", "investigation", "accused", "victim", "hurt",
        "kidnapping", "extortion", "forgery", "defamation", "trespass"
    ]
    
    @classmethod
    def validate_legal_query(cls, query: str) -> ValidationResult:
        """
        Validate a legal query input.
        
        Args:
            query: The user's legal query
            
        Returns:
            ValidationResult with validation status and details
        """
        warnings = []
        extracted_info = {}
        
        # Check if query is empty or None
        if not query or not query.strip():
            return ValidationResult(
                is_valid=False,
                message="Query cannot be empty. Please describe your legal issue.",
                warnings=[]
            )
        
        # Sanitize input
        sanitized = cls._sanitize_text(query)
        
        # Check length
        if len(sanitized) < cls.MIN_QUERY_LENGTH:
            return ValidationResult(
                is_valid=False,
                message=f"Query is too short. Please provide at least {cls.MIN_QUERY_LENGTH} characters describing your legal issue.",
                sanitized_input=sanitized
            )
        
        if len(sanitized) > cls.MAX_QUERY_LENGTH:
            warnings.append(f"Query exceeds {cls.MAX_QUERY_LENGTH} characters and will be truncated.")
            sanitized = sanitized[:cls.MAX_QUERY_LENGTH]
        
        # Check for harmful content
        for pattern in cls.HARMFUL_PATTERNS:
            if re.search(pattern, sanitized, re.IGNORECASE):
                return ValidationResult(
                    is_valid=False,
                    message="Query contains potentially harmful content. Please remove any scripts or code.",
                    warnings=[]
                )
        
        # Detect legal domain
        query_lower = sanitized.lower()
        if any(keyword in query_lower for keyword in cls.CRIMINAL_KEYWORDS):
            extracted_info["detected_domain"] = LegalDomain.CRIMINAL.value
        
        # Check for specific entities (names, dates, amounts)
        entities = cls._extract_entities(sanitized)
        if entities:
            extracted_info["entities"] = entities
        
        # Add warning if query is vague
        if len(sanitized.split()) < 10:
            warnings.append("Your query seems brief. Providing more details will help generate better results.")
        
        return ValidationResult(
            is_valid=True,
            message="Query validated successfully.",
            warnings=warnings,
            sanitized_input=sanitized,
            extracted_info=extracted_info
        )
    
    @classmethod
    def validate_document_request(cls, request: str) -> ValidationResult:
        """
        Validate a document generation request.
        
        Args:
            request: The user's document request
            
        Returns:
            ValidationResult with validation status and details
        """
        warnings = []
        extracted_info = {}
        
        # Check if request is empty
        if not request or not request.strip():
            return ValidationResult(
                is_valid=False,
                message="Document request cannot be empty. Please describe what document you need.",
                warnings=[]
            )
        
        # Sanitize input
        sanitized = cls._sanitize_text(request)
        
        # Check length
        if len(sanitized) < cls.MIN_DOCUMENT_REQUEST_LENGTH:
            return ValidationResult(
                is_valid=False,
                message=f"Please provide more details (at least {cls.MIN_DOCUMENT_REQUEST_LENGTH} characters) about the document you need.",
                sanitized_input=sanitized
            )
        
        if len(sanitized) > cls.MAX_DOCUMENT_REQUEST_LENGTH:
            warnings.append("Request is very long. Key details at the beginning will be prioritized.")
            sanitized = sanitized[:cls.MAX_DOCUMENT_REQUEST_LENGTH]
        
        # Detect document type
        request_lower = sanitized.lower()
        detected_type = DocumentType.GENERAL
        
        for doc_type, keywords in cls.DOCUMENT_KEYWORDS.items():
            if any(keyword in request_lower for keyword in keywords):
                detected_type = doc_type
                break
        
        extracted_info["detected_document_type"] = detected_type.value
        
        # Check for required information based on document type
        missing_info = cls._check_required_info(sanitized, detected_type)
        if missing_info:
            warnings.extend([f"Consider providing: {info}" for info in missing_info])
        
        # Extract entities
        entities = cls._extract_entities(sanitized)
        if entities:
            extracted_info["entities"] = entities
        
        return ValidationResult(
            is_valid=True,
            message="Document request validated successfully.",
            warnings=warnings,
            sanitized_input=sanitized,
            extracted_info=extracted_info
        )
    
    @classmethod
    def _sanitize_text(cls, text: str) -> str:
        """Sanitize text by removing harmful content and normalizing whitespace."""
        # Remove any null bytes
        text = text.replace('\x00', '')
        
        # Remove excessive whitespace
        text = ' '.join(text.split())
        
        # Remove potential script injections
        for pattern in cls.HARMFUL_PATTERNS:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
        return text.strip()
    
    @classmethod
    def _extract_entities(cls, text: str) -> Dict[str, List[str]]:
        """Extract potential legal entities from text."""
        entities = {}
        
        # Extract potential dates
        date_patterns = [
            r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',  # DD/MM/YYYY or MM/DD/YYYY
            r'\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}',
        ]
        dates = []
        for pattern in date_patterns:
            dates.extend(re.findall(pattern, text, re.IGNORECASE))
        if dates:
            entities["dates"] = dates[:5]  # Limit to first 5
        
        # Extract potential amounts
        amount_patterns = [
            r'(?:Rs\.?|₹|INR)\s*[\d,]+(?:\.\d{2})?',
            r'[\d,]+(?:\.\d{2})?\s*(?:rupees|lakhs?|crores?)',
        ]
        amounts = []
        for pattern in amount_patterns:
            amounts.extend(re.findall(pattern, text, re.IGNORECASE))
        if amounts:
            entities["amounts"] = amounts[:5]
        
        return entities
    
    @classmethod
    def _check_required_info(cls, text: str, doc_type: DocumentType) -> List[str]:
        """Check for commonly required information based on document type."""
        missing = []
        text_lower = text.lower()
        
        # Common requirements for all documents
        if not re.search(r'(?:name|party|between)', text_lower):
            missing.append("names of parties involved")
        
        if not re.search(r'(?:date|duration|period|term)', text_lower):
            missing.append("relevant dates or time periods")
        
        # Document-specific requirements
        if doc_type == DocumentType.RENTAL_AGREEMENT:
            if not re.search(r'(?:rent|amount|₹|rs)', text_lower):
                missing.append("rent amount")
            if not re.search(r'(?:address|property|location|premises)', text_lower):
                missing.append("property address")
        
        elif doc_type == DocumentType.SALE_DEED:
            if not re.search(r'(?:price|consideration|amount)', text_lower):
                missing.append("sale price/consideration")
            if not re.search(r'(?:property|land|house|flat|plot)', text_lower):
                missing.append("property details")
        
        elif doc_type == DocumentType.EMPLOYMENT_AGREEMENT:
            if not re.search(r'(?:salary|compensation|ctc|pay)', text_lower):
                missing.append("salary/compensation details")
            if not re.search(r'(?:designation|role|position|job)', text_lower):
                missing.append("job designation/role")
        
        return missing


# Convenience functions
def validate_legal_query(query: str) -> ValidationResult:
    """Validate a legal query input."""
    return InputValidator.validate_legal_query(query)


def validate_document_request(request: str) -> ValidationResult:
    """Validate a document generation request."""
    return InputValidator.validate_document_request(request)


def sanitize_input(text: str) -> str:
    """Sanitize user input text."""
    return InputValidator._sanitize_text(text)
