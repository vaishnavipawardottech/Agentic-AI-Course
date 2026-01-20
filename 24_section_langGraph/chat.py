import os
from dotenv import load_dotenv
load_dotenv()
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model = "gemini-2.0-flash-lite",
    api_key = os.getenv("API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)


class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

def samplenode(state: State):
    print("Inside samplenode node", state)
    return {"messages": ["Sample message appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, my name is vaishnavi"]}))
print("Updated State:", updated_state)
