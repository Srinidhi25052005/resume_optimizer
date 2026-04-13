import streamlit as st
from services.pdf_service import extract_text_from_pdf
from services.docx_service import extract_text_from_docx
from services.ai_service import optimize_resume

st.title("ATS Resume Optimizer 🚀")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)
    except RuntimeError as e:
        st.error(f"Could not read file: {e}")
        text = None

    if not text:
        st.warning("Could not extract text from the uploaded file. Please try another file.")
    else:
        st.text_area("Extracted Resume", text, height=300)

        if st.button("Optimize Resume"):
            try:
                result = optimize_resume(text)
                st.subheader("Optimized Resume")
                st.write(result)
            except RuntimeError as e:
                st.error(f"Optimization failed: {e}")
