from PyPDF2 import PdfReader


def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Failed to read PDF file: {e}") from e
