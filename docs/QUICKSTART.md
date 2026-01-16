# ⚡ QUICK START GUIDE

## 🎯 What Your App Does Now

✅ **Dual Purpose Application:**
1. **📋 Create Professional Legal Documents** (NEW)
   - Rental agreements, contracts, notices, etc.
   - Smart validation & clarification questions
   - Professional formatting & PDF export

2. **🔍 Analyze Criminal Cases** (Original)
   - Find applicable IPC sections
   - Retrieve legal precedents
   - Generate case analysis

---

## 🚀 Start Using (3 Minutes)

### Option 1: Web Interface (RECOMMENDED)
```bash
streamlit run app.py
```
✅ Opens web browser at http://localhost:8501  
✅ Click sidebar to choose mode  
✅ User-friendly interface  

### Option 2: Create Documents from CLI
```bash
python draft_document.py
```
✅ Type your document request  
✅ System asks clarifying questions  
✅ Saves to `exports/` folder  

### Option 3: Analyze Criminal Cases
```bash
python main.py
```
✅ Analyzes sample case included  
✅ Edit the sample case to try your own  

---

## 📝 Example: Generate a Rental Agreement

### On Web Interface:
1. **Select:** "📋 Create Legal Document" (top sidebar)
2. **Enter:** "I need a rental agreement. Property: 2BHK in Delhi. Owner: Mr. Singh. Tenant: Mr. Kumar. Rent: 25,000/month. Duration: 2 years."
3. **Click:** "📝 Generate Legal Document"
4. **Wait:** 30-60 seconds
5. **Download:** Click "📄 Download as TXT" or see formatting options

### Result:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESIDENTIAL LEASE AGREEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THIS AGREEMENT made on [Date]

BETWEEN
Mr. Singh (Owner)
AND
Mr. Kumar (Tenant)

1. PROPERTY DETAILS
   Address: 2BHK Apartment, Delhi
   Monthly Rent: Rs. 25,000

2. TERM
   Duration: 2 years
   Commencement: [Date]
   
3. PAYMENT TERMS
   Rent payable monthly on [Date]
   Security Deposit: Rs. 75,000

... [Full agreement with all clauses]
```

✅ Professional, complete, ready to use!

---

## 🔍 Example: Analyze Criminal Case

### On Web Interface:
1. **Select:** "🔍 Analyze Criminal Case (IPC)"
2. **Enter:** "My house was broken into. Thieves stole jewelry worth 2 lakhs. They threatened me with a knife."
3. **Click:** "🔍 Analyze Criminal Case"
4. **Get:** IPC sections found + precedent cases

### Result:
```
APPLICABLE IPC SECTIONS:
- Section 380: Theft in dwelling house (7-year punishment)
- Section 506: Criminal intimidation (2-year punishment)
- Section 454: House breaking (7-year punishment)

PRECEDENT CASES:
- State vs. Raj (2020): Similar burglary case
- State vs. Kumar (2019): Breaking and entering

RECOMMENDATIONS:
File FIR under Sections 380, 454, 506 IPC
```

✅ Complete legal analysis with sections and precedents!

---

## 📊 Files Generated

### When Creating Documents:
- Saved to: `exports/legal_document_[timestamp].txt`
- You can:
  - Open in Word/Google Docs
  - Download as PDF
  - Print directly
  - Share with lawyer for review

### Example Filename:
```
exports/legal_document_20260115_161030.txt
```

---

## ⚙️ Setup (If Not Done)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add API Keys to .env
```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### 3. Test System
```bash
python test_project.py
```
✅ Should show "ALL SYSTEMS OPERATIONAL"

---

## 📱 Command Reference

| Command | Purpose | Use Case |
|---------|---------|----------|
| `streamlit run app.py` | Web interface | Easy UI, both modes |
| `python draft_document.py` | Create documents | CLI document generation |
| `python main.py` | Criminal analysis | CLI criminal case analysis |
| `python test_project.py` | Verify setup | Check if everything works |
| `python query_vectordb.py` | Test IPC database | Check IPC section search |

---

## 🎨 Web Interface Guide

### Sidebar Options:
- **📋 Create Legal Document** - Generate any legal document
- **🔍 Analyze Criminal Case (IPC)** - Analyze criminal cases

### Document Creation Mode:
1. Enter your document request in text area
2. Click "📝 Generate Legal Document"
3. Wait for processing (3 colored status updates)
4. Review formatted document
5. Download as TXT/PDF

### Criminal Analysis Mode:
1. Describe the case in text area
2. Click "🔍 Analyze Criminal Case"
3. Get IPC sections and precedents
4. See complete analysis

---

## ❓ FAQ

**Q: How long does document generation take?**  
A: Usually 30-60 seconds depending on complexity.

**Q: Can I edit the generated document?**  
A: Yes! Download as TXT and edit in any text editor.

**Q: Is this legally binding?**  
A: No. Always have a lawyer review before official use.

**Q: What document types are supported?**  
A: Contracts, agreements, notices, affidavits, wills, etc.

**Q: Can I use for non-Indian documents?**  
A: System optimized for Indian context. May work for others.

**Q: How do I export to PDF?**  
A: Download TXT and print to PDF using browser.

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| ".env file not found" | Create `.env` with API keys in project root |
| Slow on first run | First run downloads models (~500MB). Next runs faster |
| Web interface not loading | Check if port 8501 is available |
| Documents not exporting | Ensure `exports/` folder exists |
| API key errors | Verify keys in `.env` file are correct |

---

## 📚 Detailed Docs

- **README.md** - Complete feature guide
- **EXPANSION_SUMMARY.md** - What was added
- **PROJECT_STATUS.md** - System status report

---

## 🎯 Next Steps

1. ✅ Start web interface: `streamlit run app.py`
2. ✅ Try creating a document
3. ✅ Try analyzing a case
4. ✅ Download and review documents
5. ✅ Customize with your own examples

---

## ✨ You're All Set!

Your AI Legal Assistant is ready to:
- ✅ Generate professional legal documents
- ✅ Analyze criminal cases with IPC sections
- ✅ Find legal precedents
- ✅ Export to multiple formats

**Start now:** `streamlit run app.py`

---

Happy drafting! 📝⚖️

---

*Last Updated: January 15, 2026*  
*Version: 2.0 (Document Drafting Edition)*
