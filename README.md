# Resume Optimizer

An ATS (Applicant Tracking System) resume optimizer built with Streamlit and Google Generative AI.

## Features

- Upload your resume in PDF or DOCX format
- Extracts resume text automatically
- Uses Google Gemini AI to analyze and optimize your resume for ATS compatibility
- Provides an ATS score, improvement suggestions, and an optimized resume

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

4. **Configure your API key**

   Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
resume_optimizer/
├── app.py              # Main Streamlit application
├── config.py           # API key configuration
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── services/
│   ├── ai_service.py   # Google Generative AI integration
│   ├── docx_service.py # DOCX text extraction
│   └── pdf_service.py  # PDF text extraction
└── .env                # Environment variables (not committed)
```

