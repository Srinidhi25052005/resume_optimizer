# resume_optimizer

An ATS Resume Optimizer built with Streamlit and Google Generative AI. Upload a PDF or DOCX resume, extract its text, and get AI-powered suggestions to improve your ATS score.

## Features

- Upload PDF or DOCX resumes
- Extract resume text automatically
- Get ATS score and improvement suggestions powered by AI

## Project Structure

```
resume_optimizer/
├── app.py               # Streamlit application entry point
├── config.py            # Environment variable configuration
├── utils.py             # Shared text extraction utilities
├── requirements.txt     # Python dependencies
├── services/
│   ├── ai_service.py    # AI optimization logic
│   ├── docx_service.py  # DOCX text extraction
│   └── pdf_service.py   # PDF text extraction
└── .env                 # Environment variables (not committed)
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
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Environment Variables

| Variable           | Description                  |
|--------------------|------------------------------|
| `GOOGLE_API_KEY`   | Google Generative AI API key |
| `GROQ_API_KEY`     | Groq API key (optional)      |
| `ANTHROPIC_API_KEY`| Anthropic API key (optional) |
