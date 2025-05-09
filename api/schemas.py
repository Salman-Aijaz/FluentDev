from pydantic import BaseModel

class ScriptRequest(BaseModel):
    topic: str
    technical: bool
    challenging: bool
    detailed: bool
    budget: bool

class GraphState(BaseModel):
    topic: str
    technical: bool
    challenging: bool
    detailed: bool
    budget: bool
    script: str = ""