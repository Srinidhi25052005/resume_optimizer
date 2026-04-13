from dotenv import load_dotenv
import os
import sys

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    sys.exit(
        "Error: GOOGLE_API_KEY is not set. "
        "Please add your Google API key to the .env file."
    )

