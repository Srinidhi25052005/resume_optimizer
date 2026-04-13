import re
import streamlit as st
from services.pdf_service import extract_text_from_pdf
from services.docx_service import extract_text_from_docx
from services.ai_service import optimize_resume

st.title("ATS Resume Optimizer 🚀")

BULLET_PREFIX_PATTERN = re.compile(r"^[\s\-\*\d\.\)\u2022]+")


def parse_ai_result(result_text):
    score = None
    suggestions = []
    optimized_resume = ""

    if not result_text:
        return score, suggestions, optimized_resume

    score_match = re.search(
        r"ATS[_\s]*SCORE\s*[:\-]\s*(\d{1,2}|100)", result_text, re.IGNORECASE
    )
    if score_match:
        score_value = int(score_match.group(1))
        score = max(0, min(score_value, 100))

    suggestions_match = re.search(r"IMPROVEMENT[_\s]*SUGGESTIONS\s*:\s*", result_text, re.IGNORECASE)
    optimized_match = re.search(r"OPTIMIZED[_\s]*RESUME\s*:\s*", result_text, re.IGNORECASE)

    suggestions_block = ""
    if suggestions_match and optimized_match:
        suggestions_block = result_text[suggestions_match.end() : optimized_match.start()].strip()
        optimized_resume = result_text[optimized_match.end() :].strip()
    elif optimized_match:
        optimized_resume = result_text[optimized_match.end() :].strip()

    if suggestions_block:
        for line in suggestions_block.splitlines():
            cleaned = BULLET_PREFIX_PATTERN.sub("", line).strip()
            if cleaned:
                suggestions.append(cleaned)
        if not suggestions and suggestions_block.strip():
            suggestions = [suggestions_block.strip()]

    return score, suggestions, optimized_resume

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    if text:
        st.text_area("Extracted Resume", text, height=300)

        if st.button("Optimize Resume"):
            with st.spinner("Optimizing your resume..."):
                result = optimize_resume(text)

            if result.startswith("Error:"):
                st.error(result)
            else:
                score, suggestions, optimized_resume = parse_ai_result(result)

                st.subheader("Results")
                if score is not None:
                    st.metric("ATS Score", f"{score}/100")
                    st.progress(score / 100)
                else:
                    st.info("ATS score not found in the response.")

                with st.expander("Improvement Suggestions"):
                    if suggestions:
                        st.markdown("\n".join(f"- {item}" for item in suggestions))
                    else:
                        st.write("No suggestions could be parsed from the response.")

                st.subheader("Optimized Resume")
                if optimized_resume:
                    st.text_area("Optimized Resume", optimized_resume, height=300)
                    st.download_button(
                        "Download Optimized Resume",
                        data=optimized_resume,
                        file_name="optimized_resume.txt",
                        mime="text/plain",
                    )
                else:
                    st.write(result)
    else:
        st.error("Failed to extract text from the uploaded file. Please try again.")
