import google.generativeai as genai
from config import api_key

genai.configure(api_key=api_key)


def optimize_resume(resume_text):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = (
            "You are an expert ATS (Applicant Tracking System) resume optimizer. "
            "Review the following resume and provide:\n"
            "1. An ATS compatibility score out of 100\n"
            "2. Specific improvements to make the resume more ATS-friendly\n"
            "3. An optimized version of the resume\n\n"
            f"Resume:\n{resume_text}"
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error optimizing resume: {e}"
