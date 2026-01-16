# document_export_tool.py

import os
from datetime import datetime
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("Document Export Tool")
def export_document(document_content: str, format_type: str = "txt", filename: str = None) -> dict:
    """
    Export a legal document to various formats (TXT, PDF, DOCX).
    
    Args:
        document_content (str): The complete formatted legal document content
        format_type (str): Export format - 'txt', 'pdf', or 'docx' (default: 'txt')
        filename (str): Custom filename without extension (optional)
    
    Returns:
        dict: Export status with file path and instructions
    """
    try:
        # Create exports directory if it doesn't exist
        exports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exports")
        os.makedirs(exports_dir, exist_ok=True)
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"legal_document_{timestamp}"
        
        # Clean filename
        filename = filename.replace(" ", "_").replace("/", "_")
        
        results = {}
        
        # Export as TXT
        if format_type.lower() in ["txt", "all"]:
            txt_path = os.path.join(exports_dir, f"{filename}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(document_content)
            results["txt"] = {
                "status": "success",
                "path": txt_path,
                "message": f"Document exported to: {txt_path}"
            }
        
        # Export as DOCX
        if format_type.lower() in ["docx", "all"]:
            try:
                from docx import Document
                from docx.shared import Pt, Inches
                from docx.enum.text import WD_ALIGN_PARAGRAPH
                
                doc = Document()
                
                # Parse document content and add to DOCX
                lines = document_content.split("\n")
                for line in lines:
                    if line.strip():
                        # Add paragraph
                        p = doc.add_paragraph(line)
                        p.paragraph_format.space_after = Pt(6)
                
                docx_path = os.path.join(exports_dir, f"{filename}.docx")
                doc.save(docx_path)
                
                results["docx"] = {
                    "status": "success",
                    "path": docx_path,
                    "message": f"Document exported to: {docx_path}"
                }
            except ImportError:
                results["docx"] = {
                    "status": "error",
                    "message": "python-docx not available. Install with: pip install python-docx"
                }
        
        # Export as PDF
        if format_type.lower() in ["pdf", "all"]:
            try:
                from reportlab.lib.pagesizes import letter
                from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
                from reportlab.lib.units import inch
                
                pdf_path = os.path.join(exports_dir, f"{filename}.pdf")
                
                doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.5*inch)
                story = []
                styles = getSampleStyleSheet()
                
                # Create custom style for legal document
                legal_style = ParagraphStyle(
                    'Legal',
                    parent=styles['Normal'],
                    fontSize=11,
                    fontName='Courier',
                    alignment=0,
                    spaceAfter=6,
                    leading=14
                )
                
                # Parse and add content
                lines = document_content.split("\n")
                for line in lines:
                    if line.strip():
                        story.append(Paragraph(line, legal_style))
                
                doc.build(story)
                
                results["pdf"] = {
                    "status": "success",
                    "path": pdf_path,
                    "message": f"Document exported to: {pdf_path}"
                }
            except ImportError:
                results["pdf"] = {
                    "status": "error",
                    "message": "reportlab not available. Install with: pip install reportlab"
                }
        
        return {
            "overall_status": "success",
            "exports": results,
            "exports_directory": exports_dir,
            "note": "All exported documents are saved in the 'exports' folder"
        }
    
    except Exception as e:
        return {
            "overall_status": "error",
            "message": f"Export failed: {str(e)}"
        }


@tool("Document Preview Tool")
def preview_document(document_content: str, lines_to_show: int = 50) -> str:
    """
    Preview a document before exporting (show first N lines).
    
    Args:
        document_content (str): The document content to preview
        lines_to_show (int): Number of lines to display (default: 50)
    
    Returns:
        str: Preview of the document
    """
    lines = document_content.split("\n")
    preview = "\n".join(lines[:lines_to_show])
    
    if len(lines) > lines_to_show:
        preview += f"\n\n... [Document continues for {len(lines) - lines_to_show} more lines]"
    
    return preview
