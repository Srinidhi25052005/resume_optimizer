import google.generativeai as genai
from config import api_key

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")


def optimize_resume(resume_text):
    try:
        prompt = f"""
You are an expert ATS (Applicant Tracking System) resume optimizer.
Analyze the following resume and provide:
1. An estimated ATS score out of 100
2. Specific improvement suggestions (keywords, action verbs, quantified achievements, formatting)
3. An optimized version of the resume

Resume:
{resume_text}
"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"AI optimization failed: {e}") from e
