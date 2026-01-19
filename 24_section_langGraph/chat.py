from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("Inside chatbot node", state)
    return {"messages": ["hi, this is message from chatbot node"]}

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
