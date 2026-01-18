import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


client = OpenAI(
    api_key=os.getenv("API_KEY"),  # Your Gemini API key
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate a caption for this image in about 50 words."},
                {"type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/5756007/pexels-photo-5756007.jpeg"}}
            ]
        }
    ]
)
print("Response:", response.choices[0].message.content)