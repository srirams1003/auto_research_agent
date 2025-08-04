from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from agents.search_agent import get_research_agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow CORS for frontend (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/research")
async def research(request: QueryRequest):
    if not os.getenv("GEMINI_API_KEY"):
        return {"error": "GEMINI_API_KEY environment variable not set."}
    try:
        agent_executor = get_research_agent()
        response = agent_executor.invoke({"input": request.query})
        return {"result": response["output"]}
    except Exception as e:
        return {"error": str(e)}