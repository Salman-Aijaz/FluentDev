from fastapi import APIRouter
from api.schemas import GraphState, ScriptRequest
from langgraph.graph import StateGraph, END
from langsmith import traceable  # ✅ NEW
from nodes.input_nodes import input_node
from nodes.generate_script_node import generate_script_node
from nodes.output_node import output_node

router = APIRouter()

# Graph setup
builder = StateGraph(GraphState)
builder.add_node("InputCollector", input_node)
builder.add_node("ScriptGenerator", generate_script_node)
builder.add_node("OutputHandler", output_node)
builder.set_entry_point("InputCollector")
builder.add_edge("InputCollector", "ScriptGenerator")
builder.add_edge("ScriptGenerator", "OutputHandler")
builder.add_edge("OutputHandler", END)
graph = builder.compile()

@router.get("/")
def welcome():
    return {"message": "🧠 FluentDev is working!"}

# ✅ Traceable wrapper
@traceable(name="GenerateScriptFlow")
def run_graph(payload: dict):
    return graph.invoke(payload)

@router.post("/generate-script")
def generate_script(payload: ScriptRequest):
    result = run_graph(payload.dict())
    return result
