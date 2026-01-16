# utils/logger.py
"""
Centralized Logging Configuration for the Multi-Agent Legal Assistant.
Provides structured logging with file and console output.
"""

import os
import sys
import logging
from datetime import datetime
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class LegalAssistantLogger:
    """Custom logger with file and console handlers for the legal assistant."""
    
    _loggers = {}  # Cache for loggers
    
    def __init__(self, name: str = "legal_assistant"):
        """Initialize the logger with the given name."""
        self.name = name
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Set up and configure the logger."""
        # Return cached logger if exists
        if self.name in LegalAssistantLogger._loggers:
            return LegalAssistantLogger._loggers[self.name]
        
        # Create logger
        logger = logging.getLogger(self.name)
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        logger.setLevel(getattr(logging, log_level, logging.INFO))
        
        # Prevent duplicate handlers
        if logger.handlers:
            return logger
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        simple_formatter = logging.Formatter(
            fmt='%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        logger.addHandler(console_handler)
        
        # File handler
        log_file_path = os.getenv("LOG_FILE_PATH", "logs/app.log")
        log_dir = Path(log_file_path).parent
        log_dir.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(
            log_file_path, 
            mode='a', 
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)
        
        # Cache the logger
        LegalAssistantLogger._loggers[self.name] = logger
        
        return logger
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self.logger.debug(message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self.logger.info(message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self.logger.warning(message, **kwargs)
    
    def error(self, message: str, exc_info: bool = False, **kwargs):
        """Log error message with optional exception info."""
        self.logger.error(message, exc_info=exc_info, **kwargs)
    
    def critical(self, message: str, exc_info: bool = True, **kwargs):
        """Log critical message with exception info."""
        self.logger.critical(message, exc_info=exc_info, **kwargs)
    
    def log_agent_action(self, agent_name: str, action: str, details: Optional[str] = None):
        """Log an agent's action with structured format."""
        msg = f"[AGENT: {agent_name}] {action}"
        if details:
            msg += f" | Details: {details}"
        self.info(msg)
    
    def log_tool_usage(self, tool_name: str, query: str, result_count: int = 0):
        """Log tool usage with structured format."""
        self.info(f"[TOOL: {tool_name}] Query: '{query[:100]}...' | Results: {result_count}")
    
    def log_api_call(self, api_name: str, status: str, duration_ms: Optional[float] = None):
        """Log external API call."""
        msg = f"[API: {api_name}] Status: {status}"
        if duration_ms:
            msg += f" | Duration: {duration_ms:.2f}ms"
        self.info(msg)
    
    def log_document_generation(self, doc_type: str, status: str, filename: Optional[str] = None):
        """Log document generation activity."""
        msg = f"[DOCUMENT: {doc_type}] Status: {status}"
        if filename:
            msg += f" | File: {filename}"
        self.info(msg)


# Create a default logger instance
logger = LegalAssistantLogger("legal_assistant")


def get_logger(name: str = "legal_assistant") -> LegalAssistantLogger:
    """Get a logger instance with the specified name."""
    return LegalAssistantLogger(name)
