import google.generativeai as genai
from config import api_key


def optimize_resume(resume_text):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""You are an ATS (Applicant Tracking System) expert. Analyze the following resume and provide:
1. An ATS compatibility score out of 100
2. Specific improvements to increase the ATS score
3. An optimized version of the resume

Resume:
{resume_text}

Please provide detailed, actionable feedback."""

    response = model.generate_content(prompt)
    return response.text
