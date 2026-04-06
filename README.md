# 🧠 DocMind AI — RAG Chatbot

A production-grade document Q&A chatbot powered by Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.14-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0-teal)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-red)

## 🚀 Features
- 📄 Upload and query any PDF document
- 🔍 Semantic search using FAISS vector database
- 🤖 Runs fully offline using Mistral 7B via Ollama
- ⚡ FastAPI REST backend with Swagger docs
- 💬 Beautiful dark-themed Streamlit chat UI
- 📊 Response time, model info shown per answer

## 🛠 Tech Stack
| Layer | Technology |
|-------|-----------|
| LLM | Mistral 7B (Ollama) |
| RAG Framework | LangChain |
| Vector DB | FAISS |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Backend | FastAPI |
| Frontend | Streamlit |

## ⚙️ Setup & Run
```bash
# 1. Clone the repo
git clone https://github.com/amandayal3/docmind-ai.git
cd docmind-ai

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install langchain langchain-openai langchain-community langchain-text-splitters faiss-cpu pypdf streamlit python-dotenv fastapi uvicorn sentence-transformers ollama reportlab

# 4. Pull Mistral model
ollama pull mistral

# 5. Ingest your PDF
python backend/ingest.py

# 6. Start FastAPI
uvicorn backend.main:app --reload

# 7. Start Streamlit
streamlit run frontend/app.py
```

## 📸 Demo
Ask any question about your document and get instant AI-powered answers!