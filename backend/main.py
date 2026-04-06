from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.rag_chain import load_qa_chain

app = FastAPI(
    title="DocMind AI — RAG API",
    description="Production-grade RAG chatbot API powered by LangChain, FAISS, and Mistral.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chain = load_qa_chain()

class QueryRequest(BaseModel):
    question: str
    top_k: Optional[int] = 3

class QueryResponse(BaseModel):
    answer: str
    question: str
    response_time: float
    model: str
    status: str

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "app": "DocMind AI",
        "version": "1.0.0",
        "description": "RAG-powered document chatbot"
    }

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy", "chain": "loaded"}

@app.post("/ask", response_model=QueryResponse, tags=["Chat"])
def ask(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    try:
        start = time.time()
        result = chain.invoke(request.question)
        elapsed = round(time.time() - start, 2)
        return QueryResponse(
            answer=result,
            question=request.question,
            response_time=elapsed,
            model="mistral",
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))