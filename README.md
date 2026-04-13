# ATS Resume Optimizer 🚀

An AI-powered resume optimizer that analyzes your resume for ATS (Applicant Tracking System) compatibility and suggests improvements using Google Gemini.

## Features

- Upload a resume in **PDF** or **DOCX** format
- Automatically extract resume text
- Get an **ATS compatibility score** (out of 100)
- Receive actionable improvement suggestions
- View an **AI-optimized version** of your resume

## Project Structure

```
resume_optimizer/
├── app.py                  # Main Streamlit application
├── config.py               # Loads environment variables
├── services/
│   ├── ai_service.py       # Google Gemini AI integration
│   ├── pdf_service.py      # PDF text extraction
│   └── docx_service.py     # DOCX text extraction
├── requirements.txt        # Python dependencies
└── .env                    # API keys (not committed)
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

4. **Configure your API key**

   Copy `.env` and fill in your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Get a free API key at [Google AI Studio](https://aistudio.google.com/).

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (Streamlit will show the local URL).
2. Upload your resume (PDF or DOCX).
3. Review the extracted text.
4. Click **Optimize Resume** to get AI-powered suggestions.

## Dependencies

- [Streamlit](https://streamlit.io/) — web UI
- [google-generativeai](https://pypi.org/project/google-generativeai/) — Google Gemini AI
- [PyPDF2](https://pypi.org/project/PyPDF2/) — PDF parsing
- [python-docx](https://pypi.org/project/python-docx/) — DOCX parsing
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable loading

