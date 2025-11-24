# tools.py – You can keep this or delete it, doesn't matter anymore
import io
import pypdf
def extract_pdf_text(file_bytes: bytes) -> str:
    pdf_stream = io.BytesIO(file_bytes)
    reader = pypdf.PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()