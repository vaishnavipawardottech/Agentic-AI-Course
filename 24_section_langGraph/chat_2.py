import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END


client = ChatOpenAI(
    model = "gemini-2.0-flash-lite",
    api_key = os.getenv("API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

class state(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: state):
    print("ChatBot Node", state)
    response = client.chat.completions.create(
        model="gemini-2.0-flash-lite",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: state) -> Literal["chatbot_gemini", "endnode"]:
    print("evaluate_response Node", state)
    if True:
        return endnode
    
    return "chatbot_gemini"

def chatbot_gemini(state: state):
    print("chatbot_gemini Node", state)
    response = client.chat.completions.create(
        model="gemini-2.0-flash-lite",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ]
    )

def endnode(state: state):
    print("endnode Node", state)
    return state

graph_builder = StateGraph(state)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("endnode", endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini", "endnode")
graph_builder.add_edge("endnode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(state({"user_query": "Hi, what is 2+2?"}))

print(updated_state)