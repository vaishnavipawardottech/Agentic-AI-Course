# persona based prompting
from dotenv import load_dotenv
from openai import OpenAI

import json
load_dotenv()

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# persona based prompting:
# Persona prompting is a technique where you instruct an AI (like an LLM) to "act as" a specific character, professional, or personality (e.g., "You are a historian," "Act like a pirate") to guide its tone, knowledge focus, and response style for a more tailored output, making it useful for creative tasks but potentially inconsistent for strict accuracy.

SYSTEM_PROMPT = """
   You are an AI persona assistant named vaishnavi pawar.
   you are acting on behalf of vaishnavi pawar who is 21 years old tech enthusiastic and software developer.
   your main texh stack is javascript, react, nodejs and you are learning GenAI these days.

   Examples:
   Q: Hey
   A: hello, how can I help you?

"""


response = client.chat.completions.create(

    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey there" }
    ]
)

print("Response:", response.choices[0].message.content)