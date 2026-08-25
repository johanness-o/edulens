import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import requests

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

app = FastAPI(title="EduLens Proxy")

# Only allow requests from your actual frontend, not any origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "https://johanness-o.github.io",
    ],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class AnalyzeRequest(BaseModel):
    prompt: str

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="Server missing API key.")

    response = requests.post(
        GROQ_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}",
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "max_tokens": 8000,
            "messages": [{"role": "user", "content": req.prompt}],
        },
        timeout=60,
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Groq request failed.")

    return response.json()

@app.get("/health")
def health():
    return {"status": "ok"}
