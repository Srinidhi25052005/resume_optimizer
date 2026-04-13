from docx import Document


def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        raise ValueError(f"Failed to read DOCX file: {e}") from e
