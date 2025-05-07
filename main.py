from langgraph.graph import StateGraph, END
from nodes.input_nodes import input_node
from nodes.generate_script_node import generate_script_node
from nodes.output_node import output_node
from typing import TypedDict

class GraphState(TypedDict):
    topic: str
    script: str

builder = StateGraph(GraphState)

builder.add_node("InputCollector", input_node)
builder.add_node("ScriptGenerator", generate_script_node)
builder.add_node("OutputHandler", output_node)

builder.set_entry_point("InputCollector")
builder.add_edge("InputCollector", "ScriptGenerator")
builder.add_edge("ScriptGenerator", "OutputHandler")
builder.add_edge("OutputHandler", END)

graph = builder.compile()

if __name__ == "__main__":
    user_topic = input("🧠 Enter your topic: ")
    result = graph.invoke({"topic": user_topic})
