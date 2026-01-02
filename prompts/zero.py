from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot Prompting: Directly giving the instructions to the model.
SYATEM_PROMPT = "you should answer ony and only coding related questions. Do not answer anything else. your name is codebot. if user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYATEM_PROMPT},
        {"role": "user", "content": "hey, tell me program to reverse a string in python!"}
    ]
)

print(response.choices[0].message.content)