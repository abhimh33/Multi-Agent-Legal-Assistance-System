# utils/__init__.py
"""Utility modules for the Multi-Agent Legal Assistant."""

from utils.logger import logger, get_logger, LegalAssistantLogger
from utils.validators import (
    ValidationResult,
    InputValidator,
    validate_legal_query,
    validate_document_request,
    sanitize_input
)
from utils.exceptions import (
    LegalAssistantError,
    ValidationError,
    APIError,
    DatabaseError,
    DocumentGenerationError,
    ToolExecutionError
)

__all__ = [
    # Logger
    "logger",
    "get_logger", 
    "LegalAssistantLogger",
    # Validators
    "ValidationResult",
    "InputValidator",
    "validate_legal_query",
    "validate_document_request",
    "sanitize_input",
    # Exceptions
    "LegalAssistantError",
    "ValidationError",
    "APIError",
    "DatabaseError",
    "DocumentGenerationError",
    "ToolExecutionError"
]
