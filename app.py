# app.py

import streamlit as st
from dotenv import load_dotenv
from crew import legal_assistant_crew
from document_crew import document_drafting_crew

load_dotenv()

st.set_page_config(page_title="AI Legal Assistant", page_icon="⚖️", layout="wide")

st.title("⚖️ Professional Legal Document Assistant")
st.markdown(
    "This AI-powered assistant helps you create professional legal documents and analyze legal issues."
)

# Sidebar for mode selection
mode = st.sidebar.radio(
    "Select Mode:",
    ["📋 Create Legal Document", "🔍 Analyze Criminal Case (IPC)"],
    help="Choose whether you want to create a legal document or analyze a criminal case"
)

if mode == "📋 Create Legal Document":
    st.header("📋 Legal Document Generator")
    st.markdown(
        "Describe what legal document you need, and the system will:\n"
        "1. Validate your request\n"
        "2. Ask for missing information\n"
        "3. Analyze requirements\n"
        "4. Draft the document\n"
        "5. Format it professionally for printing or PDF export"
    )
    
    with st.form("document_form"):
        st.markdown("### What legal document do you need?")
        document_request = st.text_area(
            "Describe your document request:",
            placeholder="Example: I need a rental agreement for my property in Delhi. The tenant is Mr. Raj Kumar, rent is 25000/month, duration is 2 years starting March 1, 2024...",
            height=250
        )
        
        submitted = st.form_submit_button("📝 Generate Legal Document", use_container_width=True)
    
    if submitted:
        if not document_request.strip():
            st.warning("⚠️ Please describe what legal document you need.")
        else:
            with st.spinner("🔄 Processing your request..."):
                with st.container():
                    progress_placeholder = st.empty()
                    progress_placeholder.info("Step 1/4: Validating your request...")
                    
                    result = document_drafting_crew.kickoff(inputs={
                        "user_input": document_request,
                        "validation_result": "",
                        "analysis_result": "",
                        "draft_result": ""
                    })
            
            st.success("✅ Document Generation Complete!")
            
            # Display the final formatted document
            st.subheader("📄 Your Legal Document")
            st.markdown("---")
            
            # Create columns for document display and actions
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.text(result if isinstance(result, str) else str(result))
            
            with col2:
                st.markdown("### Download Options")
                
                document_text = result if isinstance(result, str) else str(result)
                
                # Text download
                st.download_button(
                    label="📄 Download as TXT",
                    data=document_text,
                    file_name="legal_document.txt",
                    mime="text/plain"
                )
                
                # Show export options
                st.markdown("---")
                st.markdown("**Other Formats:**")
                st.markdown("- PDF export available via print function")
                st.markdown("- Use browser's 'Print to PDF' option")

elif mode == "🔍 Analyze Criminal Case (IPC)":
    st.header("🔍 Criminal Case Analyzer")
    st.markdown(
        "Describe a criminal case, and the system will:\n"
        "- Understand the case details\n"
        "- Find applicable IPC sections\n"
        "- Retrieve matching precedent cases\n"
        "- Generate a detailed legal analysis"
    )

    with st.form("criminal_form"):
        st.markdown("### Describe the Criminal Case")
        criminal_input = st.text_area(
            "Case details:",
            placeholder="Example: A man broke into my house at night while my family was sleeping. He stole jewelry and cash from our bedroom...",
            height=250
        )
        submitted = st.form_submit_button("🔍 Analyze Criminal Case", use_container_width=True)

    if submitted:
        if not criminal_input.strip():
            st.warning("⚠️ Please describe the criminal case.")
        else:
            with st.spinner("🔎 Analyzing your case..."):
                result = legal_assistant_crew.kickoff(inputs={"user_input": criminal_input})

            st.success("✅ Case Analysis Complete!")

            # Display results
            st.subheader("📋 Analysis Results")
            st.markdown("---")
            st.markdown(result if isinstance(result, str) else str(result))
            
            # Display intermediate results if available
            st.subheader("📊 Analysis Components")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.info("**Case Understanding:** Completed")
            with col2:
                st.info("**IPC Sections:** Found")
            with col3:
                st.info("**Precedents:** Retrieved")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    <p>⚖️ AI Legal Assistant | Powered by CrewAI & Groq | For Informational Purposes Only</p>
    <p>⚠️ This tool provides AI-generated content. Always consult a qualified legal professional for official legal advice.</p>
    </div>
    """,
    unsafe_allow_html=True
)

