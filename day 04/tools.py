import pypdf
from agents import function_tool
from typing import Literal

@function_tool
def extract_pdf_text(file_bytes: bytes) -> str:
    """
    Extracts full text from any uploaded PDF.
    """
    try:
        reader = pypdf.PdfReader(file_bytes)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
