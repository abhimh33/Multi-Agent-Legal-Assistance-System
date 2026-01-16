# ⚖️ Multi-Agent Legal Assistance System

An AI-powered legal assistant built with **CrewAI**, **Groq LLaMA 3.3**, and **RAG (Retrieval-Augmented Generation)** for Indian legal documentation and criminal case analysis.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-1.8+-green.svg)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### 📄 Document Generation
- **11 Legal Document Templates**: Rental Agreement, Affidavit, Legal Notice, Power of Attorney, Contract, NDA, Employment Agreement, Will, Partnership Deed, Sale Deed, MOU
- **PDF Export**: Professional PDF generation with headers and footers
- **Auto-fill**: Automatically adds current date/time if not provided

### 🔍 Criminal Case Analysis
- **IPC Section Search**: RAG-based search across 575 Indian Penal Code sections
- **Legal Precedent Search**: Web search for relevant case laws using Tavily API
- **Multi-Agent Validation**: 4 agents cross-validate for accuracy

### 🤖 Multi-Agent Architecture
| Agent | Role |
|-------|------|
| Case Intake Agent | Understands and classifies legal issues |
| IPC Section Agent | Identifies relevant IPC sections |
| Legal Precedent Agent | Finds relevant case laws |
| Legal Drafter Agent | Drafts professional legal documents |
| Document Validator | Validates document requests |
| Document Analyzer | Analyzes requirements |
| Document Drafter | Creates document content |
| Document Formatter | Formats for professional output |

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/abhimh33/Multi-Agent-Legal-Assistance-System.git
cd Multi-Agent-Legal-Assistance-System
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys
```

5. **Build Vector Database** (first time only)
```bash
python ipc_vectordb_builder.py
```

6. **Run the application**
```bash
streamlit run app_enhanced.py
```

7. **Open in browser**
```
http://localhost:8501
```

## 🔑 API Keys Required

| Service | Purpose | Get Key |
|---------|---------|---------|
| **Groq** | LLM (LLaMA 3.3 70B) | [console.groq.com/keys](https://console.groq.com/keys) |
| **HuggingFace** | Text Embeddings | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| **Tavily** | Legal Precedent Search | [tavily.com](https://tavily.com/) |

## 📁 Project Structure

```
Multi-Agent-Legal-Assistance-System/
├── agents/                 # CrewAI Agent definitions
│   ├── case_intake_agent.py
│   ├── ipc_section_agent.py
│   ├── legal_precedent_agent.py
│   ├── legal_drafter_agent.py
│   ├── document_validator_agent.py
│   ├── document_analyzer_agent.py
│   ├── document_drafter_agent.py
│   └── document_formatter_agent.py
├── tasks/                  # CrewAI Task definitions
├── tools/                  # Custom tools
│   ├── ipc_sections_search_tool.py
│   ├── legal_precedent_search_tool.py
│   └── pdf_generator.py
├── templates/              # Legal document templates
├── utils/                  # Utilities (logging, validation, exceptions)
├── tests/                  # Test suite
├── app_enhanced.py         # Streamlit Web UI
├── crew.py                 # Legal Assistant Crew
├── document_crew.py        # Document Drafting Crew
├── ipc.json                # IPC sections data (575 sections)
├── ipc_vectordb_builder.py # Vector DB builder
├── requirements.txt        # Python dependencies
├── .env.example            # Environment template
└── README.md               # This file
```

## 🎯 Usage Examples

### Document Generation
```
I need a rental agreement for my apartment.

Details:
- Landlord: Mr.Abhi M
- Tenant: Mr.XYZ
- Rent: Rs. 25,000/month
- Property: Flat 301, Whitefield, Bengaluru
- Duration: 11 months
```

### Criminal Case Analysis
```
Someone stole my laptop from my office. 
What legal action can I take?
```

## 🛡️ How We Reduce AI Hallucination

1. **RAG (Retrieval-Augmented Generation)**: Answers based on actual IPC sections from ChromaDB
2. **Multi-Agent Validation**: Multiple agents cross-check each other's work
3. **Structured Templates**: Pre-defined legal document templates
4. **Input Validation**: Validates user input before processing

## ⚠️ Disclaimer

This tool is for **informational purposes only** and does not constitute legal advice. Always consult a qualified legal professional for official legal matters.

## 📝 License

MIT License - See [LICENSE](LICENSE) for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Abdulappa** - [GitHub](https://github.com/abhimh33)

---

⭐ Star this repo if you find it helpful!
