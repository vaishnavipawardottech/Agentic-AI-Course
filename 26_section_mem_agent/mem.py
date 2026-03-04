from openai import OpenAI
from mem0 import Memory
import os
from dotenv import load_dotenv
load_dotenv()
import json

client = OpenAI(
    api_key = os.getenv("API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)


API_KEY = os.getenv("API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": { "api_key": API_KEY, "model": "models/text-embedding-004" }
    },
    "llm": {
        "provider": "gemini",
        "config": { "api_key": API_KEY, "model": "gemini-1.5-pro" }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    }
}

mem_client = Memory.from_config(config)


user_query = input("> ")

search_memory = mem_client.search(query=user_query, user_id="vaishnavipawar")

memories = [
    f"ID: {mem.get('id')}\nMemory: {mem.get('message')}" for mem in search_memory.get("results")
]

print("found memories:", memories)

SYSTEM_PROMPT = f"""
    here is the context about the user
    {json.dumps(memories)}
"""

response = client.chat.completions.create(
    model = "gemini-1.5-flash",
    messages = [
        { "role":"system", "content":SYSTEM_PROMPT },
        { "role":"user", "content":user_query }
    ]
)

ai_response = response.choices[0].message.content

print("AI Response:", ai_response)

mem_client.add(
    user_id="vaishnavipawar",
    messages=[
        { "role":"user", "content":user_query },
        { "role":"assistant", "content":ai_response }
    ]
)

print("Memory has been saved...")