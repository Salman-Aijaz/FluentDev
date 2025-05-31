from pydantic import BaseModel

class ScriptRequest(BaseModel):
    topic: str
    technical: bool
    challenging: bool
    detailed: bool
    budget: bool    
    friendly: bool  
    formal: bool       


class GraphState(BaseModel):
    topic: str  
    technical: bool
    challenging: bool
    detailed: bool
    budget: bool
    friendly: bool  
    formal: bool    
    script: str = ""