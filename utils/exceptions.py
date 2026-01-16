# utils/exceptions.py
"""
Custom Exception Classes for the Multi-Agent Legal Assistant.
Provides structured error handling throughout the application.
"""

from typing import Optional, Dict, Any


class LegalAssistantError(Exception):
    """Base exception class for the Legal Assistant application."""
    
    def __init__(
        self, 
        message: str, 
        error_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.error_code = error_code or "UNKNOWN_ERROR"
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for logging/serialization."""
        return {
            "error_type": self.__class__.__name__,
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details
        }
    
    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message}"


class ValidationError(LegalAssistantError):
    """Exception raised when input validation fails."""
    
    def __init__(
        self, 
        message: str, 
        field: Optional[str] = None,
        invalid_value: Optional[Any] = None
    ):
        details = {}
        if field:
            details["field"] = field
        if invalid_value is not None:
            details["invalid_value"] = str(invalid_value)[:100]  # Truncate for safety
        
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            details=details
        )
        self.field = field
        self.invalid_value = invalid_value


class APIError(LegalAssistantError):
    """Exception raised when an external API call fails."""
    
    def __init__(
        self,
        message: str,
        api_name: str,
        status_code: Optional[int] = None,
        response_body: Optional[str] = None
    ):
        details = {"api_name": api_name}
        if status_code:
            details["status_code"] = status_code
        if response_body:
            details["response_body"] = response_body[:500]  # Truncate for safety
        
        super().__init__(
            message=message,
            error_code="API_ERROR",
            details=details
        )
        self.api_name = api_name
        self.status_code = status_code


class DatabaseError(LegalAssistantError):
    """Exception raised when database operations fail."""
    
    def __init__(
        self,
        message: str,
        database_type: str = "vector_db",
        query: Optional[str] = None
    ):
        details = {"database_type": database_type}
        if query:
            details["query"] = query[:200]  # Truncate for safety
        
        super().__init__(
            message=message,
            error_code="DATABASE_ERROR",
            details=details
        )
        self.database_type = database_type


class DocumentGenerationError(LegalAssistantError):
    """Exception raised when document generation fails."""
    
    def __init__(
        self,
        message: str,
        document_type: Optional[str] = None,
        stage: Optional[str] = None
    ):
        details = {}
        if document_type:
            details["document_type"] = document_type
        if stage:
            details["stage"] = stage
        
        super().__init__(
            message=message,
            error_code="DOCUMENT_GENERATION_ERROR",
            details=details
        )
        self.document_type = document_type
        self.stage = stage


class ToolExecutionError(LegalAssistantError):
    """Exception raised when a CrewAI tool execution fails."""
    
    def __init__(
        self,
        message: str,
        tool_name: str,
        input_data: Optional[str] = None
    ):
        details = {"tool_name": tool_name}
        if input_data:
            details["input_data"] = input_data[:200]  # Truncate for safety
        
        super().__init__(
            message=message,
            error_code="TOOL_EXECUTION_ERROR",
            details=details
        )
        self.tool_name = tool_name


class ConfigurationError(LegalAssistantError):
    """Exception raised when configuration is missing or invalid."""
    
    def __init__(
        self,
        message: str,
        config_key: Optional[str] = None
    ):
        details = {}
        if config_key:
            details["config_key"] = config_key
        
        super().__init__(
            message=message,
            error_code="CONFIGURATION_ERROR",
            details=details
        )
        self.config_key = config_key


class RateLimitError(APIError):
    """Exception raised when API rate limit is exceeded."""
    
    def __init__(
        self,
        message: str,
        api_name: str,
        retry_after: Optional[int] = None
    ):
        super().__init__(
            message=message,
            api_name=api_name,
            status_code=429
        )
        self.error_code = "RATE_LIMIT_ERROR"
        if retry_after:
            self.details["retry_after_seconds"] = retry_after
        self.retry_after = retry_after
