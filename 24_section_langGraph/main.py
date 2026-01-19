import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY"),  # Your Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)