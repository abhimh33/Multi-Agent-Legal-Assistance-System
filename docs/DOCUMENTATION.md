# 📚 Multi-Agent Legal Assistant - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage Guide](#usage-guide)
6. [API Reference](#api-reference)
7. [Templates Guide](#templates-guide)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

---

## Overview

The **Multi-Agent Legal Assistant** is an AI-powered system that automates legal query understanding, retrieval of relevant Indian Penal Code (IPC) sections, identification of precedent cases, and generation of structured legal documents.

### Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **Natural Language Understanding** | Understands legal problems in plain English |
| 📖 **IPC Section Retrieval** | RAG-based semantic search over 511 IPC sections |
| ⚖️ **Precedent Search** | Finds relevant case laws from Indian Kanoon |
| 📝 **Document Generation** | Creates 11+ types of professional legal documents |
| 📄 **Multi-Format Export** | PDF, TXT, and DOCX export support |
| ✅ **Input Validation** | Comprehensive validation and sanitization |
| 📊 **Logging** | Full logging for debugging and monitoring |

### Technology Stack

- **LLM**: Groq-hosted LLaMA 3.3 70B Versatile
- **Framework**: CrewAI Multi-Agent System
- **Vector DB**: ChromaDB with HuggingFace Embeddings
- **Frontend**: Streamlit
- **Search API**: Tavily for precedent research
- **PDF Generation**: ReportLab

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER INTERACTION LAYER                        │
│                    (Streamlit Web UI)                            │
├─────────────────────────────────────────────────────────────────┤
│                    VALIDATION LAYER                              │
│         (Input Validators, Sanitizers, Error Handlers)           │
├─────────────────────────────────────────────────────────────────┤
│                    ORCHESTRATOR LAYER                            │
│                    (CrewAI Crews)                                │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Legal Assistant Crew │  │    Document Drafting Crew        │ │
│  │ - Case Intake Agent  │  │ - Document Validator Agent       │ │
│  │ - IPC Section Agent  │  │ - Document Analyzer Agent        │ │
│  │ - Precedent Agent    │  │ - Document Drafter Agent         │ │
│  │ - Legal Drafter Agent│  │ - Document Formatter Agent       │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                    TOOLS LAYER                                   │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────────┐  │
│  │ IPC Search Tool │ │ Precedent Tool  │ │ PDF Generator     │  │
│  │ (ChromaDB + RAG)│ │ (Tavily API)    │ │ (ReportLab)       │  │
│  └─────────────────┘ └─────────────────┘ └───────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│                    EXTERNAL RESOURCES                            │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────────┐  │
│  │ ChromaDB        │ │ Tavily API      │ │ Groq LLaMA 3      │  │
│  │ (IPC Vectors)   │ │ (Indian Kanoon) │ │ (LLM)             │  │
│  └─────────────────┘ └─────────────────┘ └───────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Agent Descriptions

| Agent | Role | Tools |
|-------|------|-------|
| Case Intake Agent | Analyzes queries, extracts legal intent and entities | None |
| IPC Section Agent | Retrieves relevant IPC sections | IPC Search Tool |
| Legal Precedent Agent | Finds relevant case laws | Tavily Search Tool |
| Legal Drafter Agent | Generates legal analysis and documents | None |
| Document Validator Agent | Validates document requests | None |
| Document Analyzer Agent | Analyzes document requirements | None |
| Document Drafter Agent | Creates legal document content | None |
| Document Formatter Agent | Formats documents professionally | None |

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional)

### Step-by-Step Installation

```bash
# 1. Clone or navigate to the project directory
cd multi-agent-legal-assistant

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify installation
python test_project.py
```

### Quick Start

```bash
# Run the Streamlit web application
streamlit run app.py

# Or run the CLI version
python main.py
```

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# === LLM Provider (Groq) ===
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL_NAME=llama-3.3-70b-versatile

# === HuggingFace (Embeddings) ===
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2

# === Tavily Search API ===
TAVILY_API_KEY=your_tavily_api_key_here

# === Vector Database ===
PERSIST_DIRECTORY_PATH=./vectordb
IPC_COLLECTION_NAME=ipc_collection
IPC_JSON_PATH=./ipc.json

# === Logging ===
LOG_LEVEL=INFO
LOG_FILE_PATH=logs/app.log

# === Document Export ===
EXPORT_DIRECTORY=exports
```

### Obtaining API Keys

1. **Groq API Key**: https://console.groq.com/
2. **HuggingFace Token**: https://huggingface.co/settings/tokens
3. **Tavily API Key**: https://tavily.com/

---

## Usage Guide

### 1. Web Application (Recommended)

```bash
streamlit run app.py
```

The web app provides four modes:

#### 📋 Create Legal Document
- Describe your document needs in natural language
- System validates, analyzes, and generates the document
- Export to PDF, TXT, or DOCX

#### 📄 Quick Templates
- Select from 11 pre-built legal document templates
- Fill in the required fields
- Generate and download instantly

#### 🔍 Analyze Criminal Case
- Describe a criminal incident
- Get applicable IPC sections
- Receive relevant precedent cases
- Get a detailed legal analysis

### 2. CLI Usage

```python
from crew import legal_assistant_crew

# Analyze a criminal case
result = legal_assistant_crew.kickoff(inputs={
    "user_input": "A man broke into my house and stole jewelry..."
})
print(result)
```

### 3. Generate Documents Programmatically

```python
from templates.base_template import TemplateRegistry

# Get a template
template = TemplateRegistry.get_template("rental_agreement", {
    "landlord_name": "John Doe",
    "tenant_name": "Jane Smith",
    "property_address": "123 Main Street",
    "rent_amount": "25000",
    "security_deposit": "75000",
    "agreement_duration": "11 months"
})

# Generate document
document = template.generate()

# Export to PDF
from tools.pdf_generator import DocumentExporter
exporter = DocumentExporter()
result = exporter.export(document, format_type="pdf", filename="rental_agreement")
```

---

## API Reference

### Validators Module (`utils/validators.py`)

```python
from utils.validators import validate_legal_query, validate_document_request

# Validate a legal query
result = validate_legal_query("Someone stole my wallet...")
print(result.is_valid)          # True/False
print(result.message)           # Validation message
print(result.warnings)          # List of warnings
print(result.sanitized_input)   # Cleaned input
print(result.extracted_info)    # Detected domain, entities, etc.

# Validate a document request
result = validate_document_request("I need a rental agreement...")
print(result.extracted_info)    # {'detected_document_type': 'rental_agreement'}
```

### Templates Module (`templates/`)

```python
from templates.base_template import TemplateRegistry

# List available templates
templates = TemplateRegistry.list_templates()
# ['rental_agreement', 'affidavit', 'legal_notice', ...]

# Get template info
info = TemplateRegistry.get_template_info()

# Use a template
template = TemplateRegistry.get_template("nda", {
    "disclosing_party": "Company A",
    "receiving_party": "Company B",
    "purpose": "Business discussion"
})
content = template.generate()
```

### PDF Generator (`tools/pdf_generator.py`)

```python
from tools.pdf_generator import PDFGenerator, DocumentExporter

# Generate PDF from text
generator = PDFGenerator()
result = generator.generate_pdf(
    content="Your document content...",
    filename="my_document",
    title="Legal Document"
)

# Get PDF as bytes (for streaming)
exporter = DocumentExporter()
pdf_bytes = exporter.get_pdf_bytes(content, "Document Title")

# Export to multiple formats
result = exporter.export(content, format_type="all", filename="document")
```

### Logger (`utils/logger.py`)

```python
from utils.logger import get_logger

logger = get_logger("my_module")
logger.info("Processing request...")
logger.error("Something went wrong", exc_info=True)
logger.log_agent_action("Case Intake", "Processing", "Criminal case")
logger.log_tool_usage("IPC Search", "theft robbery", result_count=3)
```

---

## Templates Guide

### Available Templates

| Template | Key | Required Fields |
|----------|-----|-----------------|
| Rental Agreement | `rental_agreement` | landlord_name, tenant_name, property_address, rent_amount, security_deposit, agreement_duration |
| Affidavit | `affidavit` | deponent_name, deponent_address, purpose |
| Legal Notice | `legal_notice` | sender_name, recipient_name, subject, facts, demand |
| Power of Attorney | `power_of_attorney` | principal_name, attorney_name, powers |
| Contract | `contract` | party_a_name, party_b_name, contract_purpose |
| NDA | `nda` | disclosing_party, receiving_party, purpose |
| Employment Agreement | `employment_agreement` | employer_name, employee_name, designation, salary |
| Will | `will` | testator_name, testator_address |
| Partnership Deed | `partnership_deed` | firm_name, partners |
| Sale Deed | `sale_deed` | seller_name, buyer_name, property_details, sale_price |
| MOU | `mou` | party_a_name, party_b_name, purpose |

### Creating Custom Templates

```python
from templates.base_template import DocumentTemplate, TemplateRegistry

class CustomTemplate(DocumentTemplate):
    template_name = "Custom Document"
    template_description = "A custom legal document"
    template_category = "custom"
    
    required_fields = ["party_name", "date"]
    optional_fields = ["notes"]
    
    def get_structure(self):
        return [{"section": "main", "title": "MAIN SECTION"}]
    
    def generate(self):
        name = self.data.get("party_name", "[NAME]")
        return f"Custom document for {name}"

# Register the template
TemplateRegistry.register("custom", CustomTemplate)
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_validators.py -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run quick system check
python test_project.py
```

### Test Categories

- `test_validators.py` - Input validation tests
- `test_templates.py` - Document template tests
- `test_tools.py` - Tool functionality tests
- `test_exceptions.py` - Exception handling tests
- `test_integration.py` - Integration tests

---

## Troubleshooting

### Common Issues

#### 1. API Key Errors

```
Error: GROQ_API_KEY not found
```

**Solution**: Ensure your `.env` file exists and contains valid API keys.

#### 2. Vector Database Not Found

```
Error: Collection 'ipc_collection' not found
```

**Solution**: Rebuild the vector database:
```bash
python ipc_vectordb_builder.py
```

#### 3. Import Errors

```
ModuleNotFoundError: No module named 'crewai'
```

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4. PDF Generation Fails

```
Error: reportlab not available
```

**Solution**: Install ReportLab:
```bash
pip install reportlab
```

### Logging

Check logs for detailed error information:
```bash
# View logs
cat logs/app.log

# Tail logs in real-time
tail -f logs/app.log
```

---

## Project Structure

```
multi-agent-legal-assistant/
├── app.py                    # Streamlit web application
├── main.py                   # CLI entry point
├── crew.py                   # Legal assistant crew definition
├── document_crew.py          # Document drafting crew definition
├── ipc_vectordb_builder.py   # Vector DB builder script
├── ipc.json                  # IPC sections data (511 sections)
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
├── .gitignore               # Git ignore rules
│
├── agents/                   # CrewAI Agent definitions
│   ├── case_intake_agent.py
│   ├── ipc_section_agent.py
│   ├── legal_precedent_agent.py
│   ├── legal_drafter_agent.py
│   ├── document_validator_agent.py
│   ├── document_analyzer_agent.py
│   ├── document_drafter_agent.py
│   └── document_formatter_agent.py
│
├── tasks/                    # CrewAI Task definitions
│   ├── case_intake_task.py
│   ├── ipc_section_task.py
│   ├── legal_precedent_task.py
│   ├── legal_drafter_task.py
│   ├── document_validator_task.py
│   ├── document_analyzer_task.py
│   ├── document_drafter_task.py
│   └── document_formatter_task.py
│
├── tools/                    # CrewAI Tools
│   ├── ipc_sections_search_tool.py
│   ├── legal_precedent_search_tool.py
│   ├── document_export_tool.py
│   └── pdf_generator.py
│
├── templates/                # Document Templates
│   ├── __init__.py
│   ├── base_template.py
│   └── legal_templates.py
│
├── utils/                    # Utility Modules
│   ├── __init__.py
│   ├── logger.py
│   ├── validators.py
│   └── exceptions.py
│
├── tests/                    # Test Suite
│   ├── __init__.py
│   ├── test_validators.py
│   ├── test_templates.py
│   ├── test_tools.py
│   ├── test_exceptions.py
│   └── test_integration.py
│
├── vectordb/                 # ChromaDB Vector Database
│   └── chroma.sqlite3
│
├── logs/                     # Application Logs
│   └── app.log
│
└── exports/                  # Exported Documents
    └── (generated documents)
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Run tests: `pytest tests/ -v`
5. Commit changes: `git commit -m "Add new feature"`
6. Push to branch: `git push origin feature/new-feature`
7. Create a Pull Request

---

## License

This project is for educational and informational purposes only. 

**Disclaimer**: The generated legal documents and analysis are AI-generated content. Always consult a qualified legal professional for official legal advice.

---

## Support

For issues and questions:
- Check the [Troubleshooting](#troubleshooting) section
- Review the [logs](#logging)
- Open an issue on GitHub
