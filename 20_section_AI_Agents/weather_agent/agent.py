# chain of thought prompting
from dotenv import load_dotenv
from openai import OpenAI
import requests
import os

import json
load_dotenv()

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def run_command(cmd: str):
    result = os.system(cmd)
    return result

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    
    return "Something went wrong while fetching the weather."

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}


SYSTEM_PROMPT = """
    you're an expert AI assistant in resolving user queries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first plan what needs to be done. the plan can be the multiple steps.
    Once you think enough plan has been done, finally you can give an output.
    You can also call a tool if required from a list of available tools.
    for every tool call wait for observe step which is the output from the called tool.

    Rules:
    - strictly follow the JSON output format.
    - only run 1 step at a time.
    - the sequence of step is START (where users gives an input), PLAN (that can be steps) and finally OUTPUT (which is going to display to the user) 

    Output JSON Format:
    {{ "step": "START" | "PLAN" | "OUTPUT" |"TOOL", "Content": "string", "tool": "string", "input": "string" }}

    Available Tools:
    - get_weather(city: str): Fetches the current weather for the specified city.
    - run_command(cmd: str): takes a system linux command as a string and executes the command on user's system and returns the output from the command.

    Example 1:
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

    Example 2:
    START: What is the weather of delhi?
    PLAN: {  "step": "PLAN", "Content": "Seems like user is interested in getting weather of delhi in india." }
    PLAN: {  "step": "PLAN", "Content": "Let's see if we have any available tool from the available tools list." }
    PLAN: {  "step": "PLAN", "Content": "Great, we have a tool called get_weather that can fetch the current weather for a specified city." }
    PLAN: {  "step": "PLAN", "Content": "I need to call get_weather with the city 'delhi' as input." }
    PLAN: {  "step": "TOOL", "tool": "get_weather", "input": "delhi" }
    PLAN: {  "step": "OBSERVE", "tool": "get_weather", "input": "the temperature of delhi is 20 C" }
    PLAN: {  "step": "PLAN", "Content": "Great, I got the weather information for delhi." }
    OUTPUT: {  "step": "OUTPUT", "Content": "The current weather in delhi is 20 C with cloudy sky." }

"""


print("\n\n\n")

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]

while True:
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

        if parsed_result.get("step") == "TOOL":
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")
            print(f"calling tool: {tool_to_call} with input: {tool_input}")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"calling tool: {tool_to_call} with input: {tool_input}: {tool_response}")
            message_history.append({"role": "developer", "content": json.dumps({"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response})})
            continue
        
        if parsed_result.get("step") == "PLAN":
            print("Planning:", parsed_result.get("Content"))
            continue

        if parsed_result.get("step") == "OUTPUT":
            print("Final Output:", parsed_result.get("Content"))
            break

    print("\n\n\n")
