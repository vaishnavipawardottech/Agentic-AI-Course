# chain of thought prompting (automated reasoning)
from dotenv import load_dotenv
from openai import OpenAI

import json
load_dotenv()

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# # chain of thought(automated reasoning)

SYSTEM_PROMPT = """
    you're an expert AI assistant in resolving user queries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first plan what needs to be done. the plan can be the multiple steps.
    Once you think enough plan has been done, finally you can give an output.

    Rules:
    - strictly follow the JSON output format.
    - only run 1 step at a time.
    - the sequence of step is START (where users gives an input), PLAN (that can be steps) and finally OUTPUT (which is going to display to the user) 

    Output JSON Format:
    {{ "step": "START" | "PLAN" | "OUTPUT", "Content": "string" }}

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: {  "step": "PLAN", "Content": "Seems like user is interested in math problem." }
    PLAN: {  "step": "PLAN", "Content": "Looking at the problem, we should solve this using BODMAS rule." }
    PLAN: {  "step": "PLAN", "Content": "Yes, the BODMAS is correct thing  to be done here." }
    PLAN: {  "step": "PLAN", "Content": "first we multiply 3 * 5 which is 15." }
    PLAN: {  "step": "PLAN", "Content": "now the equation is: 2 + 15 / 10" }
    PLAN: {  "step": "PLAN", "Content": "we must perform divide which is 15 / 10 that is 1.5." }
    PLAN: {  "step": "PLAN", "Content": "now the equation is: 2 + 1.5" }
    PLAN: {  "step": "PLAN", "Content": "finally we add 2 + 1.5 which is 3.5." }
    OUTPUT: {  "step": "OUTPUT", "Content": "The result of the expression is 3.5." }

"""

print("\n\n\n")

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]

user_query = input("Enter your query: ")
message_history.append({ "role": "user", "content": user_query })

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result=response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("starting:", parsed_result.get("Content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("Planning:", parsed_result.get("Content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("Final Output:", parsed_result.get("Content"))
        break

print("\n\n\n")
