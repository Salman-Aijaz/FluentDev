from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI(title="FluentDev Script Generator API")
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
