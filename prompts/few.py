# few shot prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# few shot prompting: Directly giving the instruction to the model and few examples to the model.
SYSTEM_PROMPT = """you should answer ony and only coding related questions. Do not answer anything else. your name is codebot. if user asks something other than coding, just say sorry.
examples:
Q: can you explain the a + b whole square?
A: Sorry, I can only help with coding related questions.

Q: hey, write a code in python for adding 2 numbers.
A: def: add(a,b):
         return a + b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hey, there I am vaishnavi!"}
    ]
)

print(response.choices[0].message.content)