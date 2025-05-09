from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="FluentDev Script Generator API")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
