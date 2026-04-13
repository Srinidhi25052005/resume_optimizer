# Resume Optimizer

An ATS (Applicant Tracking System) resume optimizer built with Streamlit.

## Features

- Upload a resume in PDF or DOCX format
- Extract text from the uploaded resume
- Analyze and optimize the resume for ATS compatibility

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env` and fill in your API keys:
   ```bash
   cp .env .env.local
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
resume_optimizer/
├── app.py              # Streamlit application entry point
├── config.py           # Configuration and environment variables
├── utils.py            # Shared utility functions
├── requirements.txt    # Python dependencies
├── services/
│   ├── ai_service.py   # Resume optimization logic
│   ├── docx_service.py # DOCX text extraction
│   └── pdf_service.py  # PDF text extraction
└── .env                # Environment variables (do not commit real keys)
```
