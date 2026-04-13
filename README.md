# ATS Resume Optimizer 🚀

A Streamlit web application that extracts text from uploaded resumes (PDF or DOCX) and provides AI-powered optimization suggestions to improve ATS (Applicant Tracking System) scores.

## Features

- Upload a resume in PDF or DOCX format
- Extracts and displays the resume text
- Provides ATS score and improvement suggestions via AI

## Project Structure

```
resume_optimizer/
├── app.py               # Main Streamlit application
├── config.py            # Configuration (loads API keys from .env)
├── utils.py             # Shared text extraction utilities
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed — see .env.example)
└── services/
    ├── __init__.py
    ├── ai_service.py    # AI optimization logic
    ├── pdf_service.py   # PDF text extraction
    └── docx_service.py  # DOCX text extraction
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srinidhi25052005/resume_optimizer.git
   cd resume_optimizer
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   ```bash
   cp .env.example .env
   # Edit .env and fill in your API keys
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Environment Variables

Create a `.env` file in the project root with the following keys:

```
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```
