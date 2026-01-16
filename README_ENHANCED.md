# AI Legal Document Assistant

A powerful AI-powered legal assistant that helps users create professional legal documents and analyze criminal cases using Indian Penal Code (IPC) sections.

## Features

### 🆕 Legal Document Generator (NEW)
Create professional legal documents with AI assistance:

1. **Input Validation** - Checks if your request is legal-related and identifies missing information
2. **Smart Clarification** - Asks for missing details (names, dates, locations, parties, etc.)
3. **Document Analysis** - Identifies document type, jurisdiction, parties, and legal requirements
4. **Professional Drafting** - Creates formally structured legal documents with proper clauses
5. **Formatting** - Formats documents professionally for printing and PDF export
6. **Multiple Export Formats** - Download as TXT, DOCX, or PDF

**Supported Document Types:**
- Rental/Lease Agreements
- Purchase Agreements
- Service Agreements
- Non-Disclosure Agreements (NDA)
- Legal Notices
- Complaints and Affidavits
- Wills and Powers of Attorney
- Contracts and Memorandums
- And more...

### 🔍 Criminal Case Analyzer (Original)
Analyze criminal cases and find applicable IPC sections:

1. **Case Understanding** - Comprehends the facts and circumstances of a criminal case
2. **IPC Section Finder** - Identifies relevant Indian Penal Code sections
3. **Legal Precedent Search** - Retrieves similar cases from Indian legal databases
4. **Case Analysis** - Provides detailed legal analysis based on findings

---

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
cd d:\multi-agent-legal-assistant
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
PERSIST_DIRECTORY_PATH=./vectordb
PERSIST_DIRECTORY_NAME=vectordb
IPC_COLLECTION_NAME=ipc_collection
IPC_JSON_PATH=./ipc.json
```

### Step 4: Verify Installation
```bash
python test_project.py
```

---

## Usage

### Option 1: Web Interface (Recommended)
```bash
streamlit run app.py
```
Opens at `http://localhost:8501` with both modes available in the sidebar.

### Option 2: CLI - Create Legal Documents
```bash
python draft_document.py
```
Follow the prompts to enter your document request. The formatted document will be saved to the `exports/` folder.

### Option 3: CLI - Analyze Criminal Cases
```bash
python main.py
```
Analyzes the sample criminal case provided in the script. Modify the `user_input` variable to analyze different cases.

### Option 4: Test Environment
```bash
python test_project.py
```
Verifies all components are installed and working correctly.

---

## Workflow

### Document Creation Workflow
```
1. User enters document request
   ↓
2. Validator checks: Is it legal? Is it complete?
   ↓
3. If incomplete → Ask for missing information
   ↓
4. Analyzer identifies: Document type, jurisdiction, parties, terms
   ↓
5. Drafter creates: Professional legal document with proper structure
   ↓
6. Formatter ensures: Professional layout, numbering, spacing
   ↓
7. Export options: TXT, DOCX, PDF download
```

### Criminal Case Analysis Workflow
```
1. User describes criminal case
   ↓
2. Case Intake Agent understands the facts
   ↓
3. IPC Section Agent finds applicable sections
   ↓
4. Legal Precedent Agent retrieves similar cases
   ↓
5. Legal Drafter generates analysis and recommendations
```

---

## Project Structure

```
multi-agent-legal-assistant/
├── agents/
│   ├── case_intake_agent.py              # Criminal case understanding
│   ├── ipc_section_agent.py              # IPC section finder
│   ├── legal_precedent_agent.py          # Case law researcher
│   ├── legal_drafter_agent.py            # Criminal case analyst
│   ├── document_validator_agent.py       # (NEW) Document validator
│   ├── document_analyzer_agent.py        # (NEW) Document analyzer
│   ├── document_drafter_agent.py         # (NEW) Document drafter
│   └── document_formatter_agent.py       # (NEW) Document formatter
├── tasks/
│   ├── case_intake_task.py
│   ├── ipc_section_task.py
│   ├── legal_precedent_task.py
│   ├── legal_drafter_task.py
│   ├── document_validator_task.py        # (NEW)
│   ├── document_analyzer_task.py         # (NEW)
│   ├── document_drafter_task.py          # (NEW)
│   └── document_formatter_task.py        # (NEW)
├── tools/
│   ├── ipc_sections_search_tool.py       # Vector DB search
│   ├── legal_precedent_search_tool.py    # Web search
│   └── document_export_tool.py           # (NEW) PDF/DOCX export
├── vectordb/                              # Chroma vector database
├── exports/                               # (NEW) Generated documents location
├── app.py                                 # Streamlit web interface
├── main.py                                # Criminal case CLI
├── draft_document.py                      # (NEW) Document drafting CLI
├── crew.py                                # Criminal case orchestration
├── document_crew.py                       # (NEW) Document drafting orchestration
├── ipc_vectordb_builder.py               # Vector DB builder
├── query_vectordb.py                     # Vector DB tester
├── test_project.py                       # System verification
├── .env                                   # Environment configuration
└── requirements.txt                       # Python dependencies
```

---

## Configuration

### API Keys
1. **Groq API Key**
   - Get from: https://console.groq.com
   - Free tier available with generous limits
   
2. **Tavily API Key**
   - Get from: https://tavily.com
   - Required for legal precedent search

### Environment Variables
All configuration is in `.env` file. Key variables:
- `GROQ_API_KEY` - LLM API key
- `TAVILY_API_KEY` - Legal research API key
- `PERSIST_DIRECTORY_PATH` - Vector DB location
- `IPC_COLLECTION_NAME` - Vector DB collection name

---

## AI Models & Tools

### LLM
- **Groq Llama-3.3-70B** - Fast, accurate, cost-effective
- Models used: `llama-3.3-70b-versatile`
- Response times: 100-500ms per request

### Embeddings
- **Sentence Transformers (all-mpnet-base-v2)**
- Vector dimensions: 768
- Documents indexed: 448 IPC sections

### Search & Research
- **Chroma Vector Database** - IPC section retrieval
- **Tavily Search API** - Legal precedent search (indiankanoon.org)

---

## Features in Detail

### Document Validator
✓ Validates if request is legal-related  
✓ Checks completeness  
✓ Identifies missing information  
✓ Asks clarifying questions  
✓ Provides structured validation report

### Document Analyzer
✓ Identifies document type  
✓ Determines jurisdiction  
✓ Identifies all parties involved  
✓ Lists key terms and conditions  
✓ Outlines legal requirements  
✓ Proposes document structure

### Document Drafter
✓ Creates formal legal documents  
✓ Uses professional legal language  
✓ Includes all necessary clauses  
✓ Maintains neutral, balanced tone  
✓ Ensures completeness  
✓ Follows standard conventions

### Document Formatter
✓ Ensures professional formatting  
✓ Numbers clauses sequentially  
✓ Proper spacing and alignment  
✓ Standard paper size compliance  
✓ Quality review and verification  
✓ Print-ready output

### Export Options
✓ TXT (plain text)  
✓ DOCX (Microsoft Word)  
✓ PDF (via reportlab)  
✓ Download from web interface  
✓ Save to exports/ folder

---

## Example Usage

### Creating a Rental Agreement

**Input:**
```
I need a rental agreement for my apartment in Mumbai. 
Owner: Ms. Priya Singh
Tenant: Mr. Raj Kumar Patel
Property: 2-BHK apartment, 5th floor, Mumbai Central
Rent: 35,000 per month
Deposit: 3 months (105,000)
Duration: 2 years starting February 1, 2024
```

**Process:**
1. ✅ Validator confirms request is valid and complete
2. ✅ Analyzer identifies: Rental Agreement, Mumbai jurisdiction, 2 parties
3. ✅ Drafter creates formal agreement with all clauses
4. ✅ Formatter ensures professional presentation
5. ✅ User can download as PDF

---

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Reinstall dependencies
```bash
pip install -r requirements.txt
```

### Issue: "GROQ_API_KEY not found"
**Solution:** Check `.env` file exists in project root
```bash
echo "GROQ_API_KEY=your_key" > .env
```

### Issue: Vector DB errors
**Solution:** Rebuild vector database
```bash
python ipc_vectordb_builder.py
```

### Issue: Slow performance on first run
**Solution:** First run downloads embedding models (~500MB). Subsequent runs are faster.

### Issue: PDF export not working
**Solution:** Ensure reportlab is installed
```bash
pip install reportlab
```

---

## System Requirements

- **OS:** Windows, macOS, or Linux
- **Python:** 3.10 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 5GB (for models and databases)
- **Internet:** Required for API calls

---

## Performance

- **Response Time:** 3-10 seconds (depends on document complexity)
- **First Run:** ~30 seconds (downloads embedding models)
- **Subsequent Runs:** 5-15 seconds
- **API Calls:** Optimized with caching

---

## Limitations & Disclaimers

⚠️ **Important:**
- This is an AI-generated content tool
- Always consult qualified legal professionals for official legal advice
- Documents generated should be reviewed by a lawyer before use
- Not a substitute for professional legal services
- Covers primarily Indian legal jurisdiction

---

## Support & Improvements

### Known Limitations
- Currently optimized for Indian legal context
- Document templates are AI-generated (not standardized templates)
- Requires human review before official use

### Future Enhancements
- Standardized legal templates library
- Multi-jurisdiction support
- Document versioning and comparison
- Signature and e-sign integration
- Case management features
- Document collaboration tools

---

## License & Usage

This project is for educational and informational purposes.  
Always verify AI-generated legal documents with qualified professionals.

---

## Contact & Support

For issues, questions, or suggestions:
1. Check the troubleshooting section above
2. Review the PROJECT_STATUS.md file
3. Verify all dependencies are installed

---

**Last Updated:** January 15, 2026  
**Version:** 2.0 (With Document Drafting Features)
