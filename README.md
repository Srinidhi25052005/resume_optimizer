# Resume Optimizer 🚀

An ATS (Applicant Tracking System) resume optimizer built with Streamlit and Google Generative AI (Gemini).

## Features

- Upload a resume in **PDF** or **DOCX** format
- Extracts resume text automatically
- Uses Google Gemini AI to analyze and optimize the resume for ATS compatibility
- Provides an ATS score, improvement suggestions, and an optimized resume

## Project Structure

```
resume_optimizer/
├── app.py               # Streamlit entry point
├── config.py            # Loads environment variables
├── utils.py             # Shared utility functions
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed to git)
└── services/
    ├── __init__.py
    ├── ai_service.py    # Google Generative AI integration
    ├── docx_service.py  # DOCX text extraction
    └── pdf_service.py   # PDF text extraction
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
   source venv/bin/activate   # On Windows: venv\Scripts\activate
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
   Get a free Google Gemini API key at: https://aistudio.google.com/app/apikey

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Requirements

- Python 3.8+
- Streamlit
- google-generativeai
- python-docx
- PyPDF2
- python-dotenv

