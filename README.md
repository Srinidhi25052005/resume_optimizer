# ATS Resume Optimizer 🚀

A Streamlit web app that uploads a PDF or DOCX resume, extracts its text, and uses Google's Generative AI (Gemini) to provide ATS optimization suggestions and an improved resume.

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

4. **Add your Google API key**

   Create a `.env` file in the project root (it is git-ignored):
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
resume_optimizer/
├── app.py               # Streamlit UI
├── config.py            # Loads environment variables
├── services/
│   ├── ai_service.py    # Google Generative AI integration
│   ├── pdf_service.py   # PDF text extraction
│   └── docx_service.py  # DOCX text extraction
├── requirements.txt
└── .env                 # Your API keys (git-ignored)
```

## Features

- Upload PDF or DOCX resumes
- Automatic text extraction
- AI-powered ATS score and improvement suggestions
- Optimized resume output
