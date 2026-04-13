import google.generativeai as genai
from config import api_key


def optimize_resume(resume_text):
    if not api_key:
        return "Error: GOOGLE_API_KEY is not set. Please add it to your .env file."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
You are an ATS (Applicant Tracking System) expert. Analyze the following resume and provide:

1. An ATS compatibility score out of 100
2. Specific improvements to increase the ATS score (keywords, action verbs, quantified achievements, formatting)
3. An optimized version of the resume

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text
