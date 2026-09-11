import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Try Streamlit Cloud Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Use local .env if Streamlit Secrets are not available
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)


def ask_ai(message):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message
    )

    return response.text