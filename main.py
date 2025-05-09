from langgraph.graph import StateGraph, END
from nodes.input_nodes import input_node
from nodes.generate_script_node import generate_script_node
from nodes.output_node import output_node
from pydantic import BaseModel

class GraphState(BaseModel):
    topic: str
    technical: bool
    challenging: bool
    detailed: bool
    budget: bool
    script: str = ""

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
    technical = input("Is the client technical? (y/n): ").lower() == "y"
    challenging = input("Is the client challenging? (y/n): ").lower() == "y"
    detailed = input("Should the responses be detailed? (y/n): ").lower() == "y"
    budget = input("Include budget talk? (y/n): ").lower() == "y"

    result = graph.invoke({
        "topic": user_topic,
        "technical": technical,
        "challenging": challenging,
        "detailed": detailed,
        "budget": budget
    })

