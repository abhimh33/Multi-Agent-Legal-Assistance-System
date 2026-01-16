# app.py
"""
Multi-Agent Legal Assistant - Streamlit Web Application
Professional legal document generation and criminal case analysis.
"""

import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime
from io import BytesIO

# Load environment variables FIRST
load_dotenv()

# IMPORTANT: Disable OpenAI fallback - Force CrewAI to use Groq only
# This prevents CrewAI from using system OPENAI_API_KEY if present
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_API_BASE"] = ""

# Import crews
from crew import legal_assistant_crew
from document_crew import document_drafting_crew

# Import utilities
from utils.logger import get_logger
from utils.validators import validate_legal_query, validate_document_request
from utils.exceptions import LegalAssistantError, ValidationError

# Import templates and PDF generator
from templates.base_template import TemplateRegistry
from templates.legal_templates import *  # Register all templates
from tools.pdf_generator import PDFGenerator, DocumentExporter

# Initialize logger
logger = get_logger("streamlit_app")

# Page configuration
st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1a365d;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4a5568;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #c6f6d5;
        border-left: 4px solid #38a169;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fefcbf;
        border-left: 4px solid #d69e2e;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fed7d7;
        border-left: 4px solid #e53e3e;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #bee3f8;
        border-left: 4px solid #3182ce;
    }
    .document-preview {
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        background-color: #f7fafc;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
        max-height: 600px;
        overflow-y: auto;
    }
    .template-card {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff;
        border: 1px solid #e2e8f0;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    .template-card:hover {
        border-color: #3182ce;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)


def display_validation_result(validation_result, container):
    """Display validation result with warnings as helpful suggestions."""
    if not validation_result.is_valid:
        container.error(f"❌ {validation_result.message}")
        return False
    
    # Show warnings as helpful suggestions (not blocking)
    if validation_result.warnings:
        with container.expander("💡 Suggestions to improve your document (optional)", expanded=True):
            for warning in validation_result.warnings:
                st.info(f"💡 {warning}")
            st.caption("📝 Note: These are suggestions. You can proceed without providing all details - the system will use appropriate defaults.")
    
    # Show extracted info
    if validation_result.extracted_info:
        with container.expander("📊 Detected Information", expanded=False):
            for key, value in validation_result.extracted_info.items():
                st.write(f"**{key.replace('_', ' ').title()}:** {value}")
    
    return True


def add_default_datetime_if_missing(text: str) -> str:
    """Add current date/time to the request if not provided."""
    from datetime import datetime
    
    text_lower = text.lower()
    additions = []
    
    # Check if date is missing
    if not any(word in text_lower for word in ['date', 'dated', '/2024', '/2025', '/2026', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']):
        current_date = datetime.now().strftime("%d/%m/%Y")
        additions.append(f"Document Date: {current_date}")
    
    # Check if time is needed but missing
    if 'time' in text_lower and not any(c in text_lower for c in ['am', 'pm', ':']):
        current_time = datetime.now().strftime("%I:%M %p")
        additions.append(f"Time: {current_time}")
    
    if additions:
        return text + "\n\n[Auto-filled Information]\n" + "\n".join(additions)
    
    return text


def generate_pdf_download(content: str, filename: str, title: str):
    """Generate PDF and return download button."""
    try:
        exporter = DocumentExporter()
        pdf_bytes = exporter.get_pdf_bytes(content, title)
        
        if pdf_bytes:
            return pdf_bytes, f"{filename}.pdf"
        return None, None
    except Exception as e:
        logger.error(f"PDF generation failed: {str(e)}")
        return None, None


def main():
    """Main application function."""
    
    # Header
    st.markdown('<h1 class="main-header">⚖️ AI Legal Assistant</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Professional Legal Document Generation & Criminal Case Analysis</p>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/law.png", width=80)
        st.markdown("### Navigation")
        
        mode = st.radio(
            "Select Mode:",
            [
                "📋 Create Legal Document",
                "📄 Quick Templates",
                "🔍 Analyze Criminal Case",
                "ℹ️ About"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### Settings")
        
        # Export format preference
        export_format = st.selectbox(
            "Default Export Format:",
            ["PDF", "TXT", "DOCX", "All Formats"]
        )
        
        include_disclaimer = st.checkbox("Include Disclaimer", value=True)
        
        st.markdown("---")
        st.markdown("### Quick Links")
        st.markdown("- [📖 Documentation](README.md)")
        st.markdown("- [🐛 Report Issue](https://github.com)")
    
    # Main Content Area
    if mode == "📋 Create Legal Document":
        render_document_generator(export_format, include_disclaimer)
    
    elif mode == "📄 Quick Templates":
        render_quick_templates(export_format)
    
    elif mode == "🔍 Analyze Criminal Case":
        render_case_analyzer()
    
    elif mode == "ℹ️ About":
        render_about()
    
    # Footer
    st.markdown("---")
    render_footer()


def render_document_generator(export_format: str, include_disclaimer: bool):
    """Render the document generation interface."""
    
    st.header("📋 Legal Document Generator")
    
    st.markdown("""
    Describe what legal document you need, and the AI system will:
    1. ✅ Validate your request
    2. 📝 Analyze requirements  
    3. ⚖️ Draft the document
    4. 📄 Format for professional use
    """)
    
    # Document type hints
    with st.expander("💡 Supported Document Types", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **Property:**
            - Rental Agreement
            - Sale Deed
            - Lease Agreement
            """)
        with col2:
            st.markdown("""
            **Legal:**
            - Affidavit
            - Legal Notice
            - Power of Attorney
            """)
        with col3:
            st.markdown("""
            **Business:**
            - NDA
            - Contract
            - Employment Agreement
            """)
    
    # Input form
    with st.form("document_form", clear_on_submit=False):
        document_request = st.text_area(
            "Describe your document request:",
            placeholder="""Example: I need a rental agreement for my 2BHK apartment in Delhi.

Details:
- Landlord: Mr. Rajesh Kumar
- Tenant: Ms. Priya Sharma  
- Rent: Rs. 25,000 per month
- Security Deposit: Rs. 75,000
- Duration: 11 months starting February 1, 2024
- Property: Flat No. 301, Green Valley Apartments, Sector 15, Delhi""",
            height=250,
            key="doc_request"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button(
                "📝 Generate Legal Document",
                use_container_width=True,
                type="primary"
            )
        with col2:
            clear = st.form_submit_button("🗑️ Clear", use_container_width=True)
    
    # Process request
    if submitted and document_request.strip():
        logger.info(f"Document generation requested: {document_request[:100]}...")
        
        # Validation
        validation_container = st.container()
        validation_result = validate_document_request(document_request)
        
        if not display_validation_result(validation_result, validation_container):
            return
        
        # Add current date/time if missing
        enhanced_request = add_default_datetime_if_missing(
            validation_result.sanitized_input or document_request
        )
        
        # Generate document
        with st.spinner("🔄 Generating your legal document... This may take a moment."):
            try:
                # Progress indicators
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Step 1/4: Validating request...")
                progress_bar.progress(25)
                
                result = document_drafting_crew.kickoff(inputs={
                    "user_input": enhanced_request,
                    "validation_result": "",
                    "analysis_result": "",
                    "draft_result": ""
                })
                
                progress_bar.progress(100)
                status_text.text("✅ Document generation complete!")
                
                logger.info("Document generated successfully")
                
                # Display result
                document_text = result if isinstance(result, str) else str(result)
                
                st.success("✅ Document Generated Successfully!")
                
                # Create tabs for different views
                tab1, tab2 = st.tabs(["📄 Document Preview", "📥 Download Options"])
                
                with tab1:
                    st.markdown('<div class="document-preview">', unsafe_allow_html=True)
                    st.text(document_text)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with tab2:
                    st.markdown("### Export Your Document")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    # TXT Download
                    with col1:
                        st.download_button(
                            label="📄 Download TXT",
                            data=document_text,
                            file_name=f"legal_document_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    # PDF Download
                    with col2:
                        pdf_bytes, pdf_filename = generate_pdf_download(
                            document_text,
                            f"legal_document_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                            "Legal Document"
                        )
                        if pdf_bytes:
                            st.download_button(
                                label="📕 Download PDF",
                                data=pdf_bytes,
                                file_name=pdf_filename,
                                mime="application/pdf",
                                use_container_width=True
                            )
                        else:
                            st.button("📕 PDF (Error)", disabled=True, use_container_width=True)
                    
                    # Copy to clipboard instruction
                    with col3:
                        st.info("💡 Use Ctrl+A to select all text from preview, then Ctrl+C to copy")
                
            except Exception as e:
                logger.error(f"Document generation failed: {str(e)}", exc_info=True)
                st.error(f"❌ Error generating document: {str(e)}")
    
    elif submitted:
        st.warning("⚠️ Please describe what legal document you need.")


def render_quick_templates(export_format: str):
    """Render quick template selection interface."""
    
    st.header("📄 Quick Legal Templates")
    st.markdown("Select a template and fill in the details to quickly generate a document.")
    
    # Get available templates
    templates_info = TemplateRegistry.get_template_info()
    
    # Group templates by category
    categories = {}
    for t in templates_info:
        cat = t.get("category", "general")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(t)
    
    # Template selection
    selected_template = st.selectbox(
        "Select Template:",
        options=[t["name"] for t in templates_info],
        format_func=lambda x: next(
            (t["display_name"] for t in templates_info if t["name"] == x),
            x.replace("_", " ").title()
        )
    )
    
    if selected_template:
        template = TemplateRegistry.get_template(selected_template)
        
        if template:
            st.markdown(f"**Description:** {template.template_description}")
            
            # Dynamic form based on template fields
            st.markdown("### Fill in Details")
            
            with st.form(f"template_form_{selected_template}"):
                form_data = {}
                
                # Required fields
                if template.required_fields:
                    st.markdown("**Required Fields:**")
                    for field in template.required_fields:
                        field_label = field.replace("_", " ").title()
                        form_data[field] = st.text_input(
                            f"{field_label} *",
                            key=f"req_{field}"
                        )
                
                # Optional fields
                if template.optional_fields:
                    with st.expander("Optional Fields", expanded=False):
                        for field in template.optional_fields:
                            field_label = field.replace("_", " ").title()
                            form_data[field] = st.text_input(
                                field_label,
                                key=f"opt_{field}"
                            )
                
                generate_btn = st.form_submit_button(
                    "📝 Generate Document",
                    type="primary",
                    use_container_width=True
                )
            
            if generate_btn:
                # Check required fields
                missing_fields = [
                    f for f in template.required_fields
                    if not form_data.get(f)
                ]
                
                if missing_fields:
                    st.error(f"❌ Please fill in required fields: {', '.join(missing_fields)}")
                else:
                    # Generate document
                    template_with_data = TemplateRegistry.get_template(selected_template, form_data)
                    document_text = template_with_data.generate()
                    
                    st.success("✅ Document Generated!")
                    
                    # Preview and download
                    tab1, tab2 = st.tabs(["📄 Preview", "📥 Download"])
                    
                    with tab1:
                        st.text(document_text)
                    
                    with tab2:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.download_button(
                                "📄 Download TXT",
                                data=document_text,
                                file_name=f"{selected_template}_{datetime.now().strftime('%Y%m%d')}.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        
                        with col2:
                            pdf_bytes, pdf_filename = generate_pdf_download(
                                document_text,
                                f"{selected_template}_{datetime.now().strftime('%Y%m%d')}",
                                template.template_name
                            )
                            if pdf_bytes:
                                st.download_button(
                                    "📕 Download PDF",
                                    data=pdf_bytes,
                                    file_name=pdf_filename,
                                    mime="application/pdf",
                                    use_container_width=True
                                )


def render_case_analyzer():
    """Render the criminal case analysis interface."""
    
    st.header("🔍 Criminal Case Analyzer (IPC)")
    
    st.markdown("""
    Describe a criminal case, and the AI system will:
    - 🧠 Understand the case details
    - 📖 Find applicable IPC sections
    - ⚖️ Retrieve matching precedent cases
    - 📝 Generate a detailed legal analysis
    """)
    
    # Example cases
    with st.expander("💡 Example Case Descriptions", expanded=False):
        st.markdown("""
        **Theft/Burglary:**
        > A man broke into my house at night while my family was sleeping. 
        > He stole jewelry and cash from our bedroom. When I confronted him, 
        > he threatened me with a knife and ran away.
        
        **Fraud/Cheating:**
        > A person sold me a plot of land showing fake documents. 
        > After I paid Rs. 50 lakhs, I discovered the land was already 
        > registered under someone else's name.
        
        **Assault:**
        > My neighbor attacked me with a wooden stick over a parking dispute.
        > I suffered head injuries and was hospitalized for 3 days.
        """)
    
    # Input form
    with st.form("criminal_form"):
        criminal_input = st.text_area(
            "Describe the Criminal Case:",
            placeholder="Describe the incident in detail including: what happened, who was involved, when and where it occurred, any evidence available...",
            height=250,
            key="criminal_input"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            submitted = st.form_submit_button(
                "🔍 Analyze Criminal Case",
                use_container_width=True,
                type="primary"
            )
        with col2:
            clear = st.form_submit_button("🗑️ Clear", use_container_width=True)
    
    # Process request
    if submitted and criminal_input.strip():
        logger.info(f"Case analysis requested: {criminal_input[:100]}...")
        
        # Validation
        validation_container = st.container()
        validation_result = validate_legal_query(criminal_input)
        
        if not display_validation_result(validation_result, validation_container):
            return
        
        # Analyze case
        with st.spinner("🔎 Analyzing your case... This may take a moment."):
            try:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Step 1/4: Understanding case details...")
                progress_bar.progress(25)
                
                result = legal_assistant_crew.kickoff(inputs={
                    "user_input": validation_result.sanitized_input or criminal_input
                })
                
                progress_bar.progress(100)
                status_text.text("✅ Analysis complete!")
                
                logger.info("Case analysis completed successfully")
                
                # Display results
                st.success("✅ Case Analysis Complete!")
                
                # Analysis components
                st.subheader("📊 Analysis Summary")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Case Understanding", "✓ Completed")
                with col2:
                    st.metric("IPC Sections", "✓ Found")
                with col3:
                    st.metric("Precedents", "✓ Retrieved")
                
                # Full analysis
                st.subheader("📋 Detailed Analysis")
                result_text = result if isinstance(result, str) else str(result)
                st.markdown(result_text)
                
                # Export options
                st.subheader("📥 Export Analysis")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.download_button(
                        "📄 Download as TXT",
                        data=result_text,
                        file_name=f"case_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col2:
                    pdf_bytes, pdf_filename = generate_pdf_download(
                        result_text,
                        f"case_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        "Criminal Case Analysis"
                    )
                    if pdf_bytes:
                        st.download_button(
                            "📕 Download as PDF",
                            data=pdf_bytes,
                            file_name=pdf_filename,
                            mime="application/pdf",
                            use_container_width=True
                        )
                
            except Exception as e:
                logger.error(f"Case analysis failed: {str(e)}", exc_info=True)
                st.error(f"❌ Error analyzing case: {str(e)}")
    
    elif submitted:
        st.warning("⚠️ Please describe the criminal case.")


def render_about():
    """Render the about page."""
    
    st.header("ℹ️ About AI Legal Assistant")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Multi-Agent Framework for Intelligent Legal Assistance
        
        This project implements a sophisticated Multi-Agent Intelligent Legal Assistant 
        that automates legal query understanding, retrieval of relevant Indian Penal Code 
        (IPC) sections, identification of precedent cases, and generation of structured 
        legal documents.
        
        #### Key Features
        
        - **🧠 Natural Language Understanding**: Understands legal problems expressed in plain English
        - **📖 IPC Section Retrieval**: Semantic search over Indian Penal Code using RAG
        - **⚖️ Precedent Search**: Finds relevant case laws from trusted sources
        - **📝 Document Generation**: Creates professional legal documents
        - **📄 Multiple Export Formats**: PDF, TXT, and DOCX support
        
        #### Technology Stack
        
        - **LLM**: Groq-hosted LLaMA 3.3 70B
        - **Framework**: CrewAI Multi-Agent System
        - **Vector DB**: ChromaDB with HuggingFace Embeddings
        - **Frontend**: Streamlit
        - **Search API**: Tavily for precedent research
        
        #### Specialized Agents
        
        1. **Case Intake Agent**: Analyzes queries and extracts legal intent
        2. **IPC Section Agent**: Retrieves relevant IPC sections
        3. **Legal Precedent Agent**: Fetches relevant case laws
        4. **Legal Drafting Agent**: Generates structured legal documents
        5. **Document Formatter Agent**: Ensures professional presentation
        """)
    
    with col2:
        st.markdown("### Quick Stats")
        st.metric("IPC Sections", "511")
        st.metric("Document Templates", "11")
        st.metric("AI Agents", "8")
        
        st.markdown("### Supported Documents")
        st.markdown("""
        - Rental Agreement
        - Sale Deed
        - Affidavit
        - Legal Notice
        - Power of Attorney
        - Contract
        - NDA
        - Employment Agreement
        - Will
        - Partnership Deed
        - MOU
        """)
    
    st.markdown("---")
    st.warning("""
    ⚠️ **Disclaimer**: This tool provides AI-generated content for informational purposes only. 
    Always consult a qualified legal professional for official legal advice. The generated 
    documents should be reviewed by a lawyer before use in legal proceedings.
    """)


def render_footer():
    """Render the application footer."""
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 12px; padding: 1rem;'>
        <p>⚖️ <strong>AI Legal Assistant</strong> | Powered by CrewAI, Groq LLaMA 3, & Streamlit</p>
        <p>© 2024 | For Informational Purposes Only</p>
        <p>⚠️ Always consult a qualified legal professional for official legal advice.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# Run the application
if __name__ == "__main__":
    main()
