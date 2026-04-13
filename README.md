# ATS Resume Optimizer 🚀

An AI-powered resume optimizer that analyzes your resume and provides ATS (Applicant Tracking System) compatibility feedback using Google Gemini.

## Features

- Upload resumes in **PDF** or **DOCX** format
- Extracts and displays resume text
- Uses Google Gemini AI to:
  - Score your resume for ATS compatibility (out of 100)
  - Suggest specific improvements
  - Return an optimized version of your resume

## Project Structure

```
resume_optimizer/
├── app.py              # Streamlit web application
├── config.py           # Loads environment variables
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed to git)
└── services/
    ├── ai_service.py   # Google Gemini AI integration
    ├── docx_service.py # DOCX text extraction
    └── pdf_service.py  # PDF text extraction
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srinidhi25052005/resume_optimizer.git
   cd resume_optimizer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**

   Copy `.env` and fill in your keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   Get a free Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (default: http://localhost:8501)
2. Upload your resume (PDF or DOCX)
3. Review the extracted text
4. Click **Optimize Resume** to get AI-powered feedback
