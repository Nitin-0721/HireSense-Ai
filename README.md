# 🤖 HireSense AI

AI-powered Resume Intelligence Platform built using FastAPI, Streamlit, FAISS and Groq Llama.

## 🚀 Features

- 📄 Upload Resume PDF
- 📋 Upload Job Description
- 🤖 Chat with Resume (RAG)
- 📊 ATS Score
- ✅ Matching Skills
- ❌ Missing Skills
- 💡 Resume Improvement Suggestions
- 🎯 AI Generated Interview Questions

## 🛠 Tech Stack

- Python
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- Groq Llama 3
- PyMuPDF

## Project Structure

```
HireSense-AI
│
├── backend
│
├── frontend
│
└── README.md
```

## Run

Backend

```bash
cd backend
venv\Scripts\activate
uvicorn app:app --reload
```

Frontend

```bash
cd frontend
python -m streamlit run frontend.py
```

## Future Improvements

- User Authentication
- Resume History
- Deployment
- Docker Support
