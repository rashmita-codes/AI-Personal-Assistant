import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load local .env file
load_dotenv()

# Get API key from Streamlit Secrets when deployed,
# otherwise get it from .env locally
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
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