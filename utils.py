from docx import Document
import PyPDF2
 
 
def extract_text_from_docx(file):
 
    try:
        doc = Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text
    except:
        return None
 
 
def extract_text_from_pdf(file):
 
    try:
        pdf_reader = PyPDF2.PdfReader(file)
 
        text = ""
 
        for page in pdf_reader.pages:
            text += page.extract_text()
 
        return text
 
    except:
        return None
 
 
