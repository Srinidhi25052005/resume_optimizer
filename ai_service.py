import google.generativeai as genai
from config import api_key

genai.configure(api_key=api_key)
_model = genai.GenerativeModel("gemini-pro")


def optimize_resume(resume_text):
    prompt = f"""You are an ATS (Applicant Tracking System) expert. Analyze the following resume and provide:
1. An ATS compatibility score out of 100
2. Specific improvements to increase the ATS score (keywords, formatting, action verbs, quantified achievements)
3. An optimized version of the resume

Resume:
{resume_text}"""

    response = _model.generate_content(prompt)
    return response.text
