from docx import Document


def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from DOCX: {e}") from e
