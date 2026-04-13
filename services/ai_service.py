import google.generativeai as genai
from config import api_key


def optimize_resume(resume_text):
    if not api_key:
        return "Error: GOOGLE_API_KEY is not set. Please add it to your .env file."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
You are an ATS (Applicant Tracking System) expert. Analyze the following resume and respond ONLY in the exact format below:

ATS_SCORE: <number between 0 and 100>
IMPROVEMENT_SUGGESTIONS:
- <suggestion 1>
- <suggestion 2>
OPTIMIZED_RESUME:
<optimized resume text>

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text
