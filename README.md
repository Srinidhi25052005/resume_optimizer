# Resume Optimizer 🚀

An ATS-friendly resume optimizer built with Streamlit and AI services.

## Features

- Upload a resume in PDF or DOCX format
- Extract text from the uploaded file
- Optimize the resume using AI to improve ATS scores

## Project Structure

```
resume_optimizer/
├── app.py               # Main Streamlit application
├── config.py            # Configuration and environment variable loading
├── utils.py             # Utility functions for text extraction
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
└── services/
    ├── ai_service.py    # AI-based resume optimization logic
    ├── docx_service.py  # DOCX text extraction
    └── pdf_service.py   # PDF text extraction
```

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   cp .env.example .env
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Environment Variables

Create a `.env` file with the following keys:

```
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```
