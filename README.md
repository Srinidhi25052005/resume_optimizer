# ATS Resume Optimizer 🚀

A Streamlit-based web app that extracts text from uploaded resumes (PDF or DOCX) and uses an AI service to provide ATS optimization suggestions.

## Project Structure

```
resume_optimizer/
├── app.py               # Streamlit entry point
├── config.py            # Loads environment variables
├── utils.py             # Shared text extraction helpers
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed — see Setup below)
└── services/
    ├── ai_service.py    # Resume optimization logic
    ├── pdf_service.py   # PDF text extraction
    └── docx_service.py  # DOCX text extraction
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
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**

   Create a `.env` file with your keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser (Streamlit prints the URL on startup).
2. Upload a resume in PDF or DOCX format.
3. Review the extracted text.
4. Click **Optimize Resume** to get ATS improvement suggestions.
