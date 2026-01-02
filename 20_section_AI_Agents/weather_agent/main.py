from openai import OpenAI
import requests

client = OpenAI(
    api_key="",  # Add your API key here or set it in the environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    
    return "Something went wrong while fetching the weather."

def main():
    user_query = input("Enter the Query: ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print("AI Response:", response.choices[0].message.content)

main()