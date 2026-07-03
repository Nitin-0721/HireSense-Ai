# 🚀 HireSense AI – RAG-based Resume Intelligence Platform

> An AI-powered Resume Intelligence Platform that enables semantic resume querying and ATS-based resume evaluation using Retrieval-Augmented Generation (RAG), FAISS Vector Search, Sentence Transformers, Groq Llama 3, FastAPI, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📌 Overview

HireSense AI is an AI-powered Resume Intelligence Platform designed to help candidates analyze and interact with their resumes using Large Language Models (LLMs).

The application performs two major tasks:

- 📄 Resume Question Answering using Retrieval-Augmented Generation (RAG)
- 🎯 ATS (Applicant Tracking System) Resume Analysis against a Job Description

Instead of sending the entire resume to the LLM every time, the project implements a Retrieval-Augmented Generation (RAG) pipeline where only the most relevant resume sections are retrieved using semantic search before generating an answer.

This significantly improves:

- Accuracy
- Context Awareness
- Response Quality
- Hallucination Reduction

The ATS module further compares the uploaded resume with a Job Description (JD) and generates:

- ATS Score
- Matching Skills
- Missing Skills
- Resume Summary
- Resume Improvement Suggestions
- AI-generated Interview Questions

---

# ✨ Features

## 📄 Resume Intelligence

- Upload Resume (PDF)
- Automatic PDF Text Extraction
- Semantic Resume Search
- Context-aware AI Chat
- Resume Question Answering
- RAG Pipeline using FAISS

---

## 🎯 ATS Analysis

- Upload Job Description
- Resume-JD Matching
- ATS Compatibility Score
- Matching Skills Detection
- Missing Skills Detection
- Resume Improvement Suggestions
- AI-generated Interview Questions

---

## 🤖 AI Capabilities

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Prompt Engineering
- Large Language Model Integration
- Context-aware Question Answering

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python

---

## Frontend

- Streamlit

---

## AI / Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- Groq API
- Llama 3.3 70B Versatile

---

## PDF Processing

- PyMuPDF (fitz)

---

## Other Libraries

- NumPy
- python-dotenv
- Requests
- JSON

---

# 🧠 Core Concepts Used

This project demonstrates several modern AI concepts:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Vector Database
- Similarity Search
- Prompt Engineering
- Large Language Models (LLMs)
- REST APIs
- Client-Server Architecture

---

# 📂 Project Structure

```
HireSense-AI
│
├── backend
│   │
│   ├── app.py
│   ├── utils.py
│   ├── rag.py
│   ├── llm.py
│   ├── ats.py
│   │
│   ├── uploads/
│   │
│   ├── routes/
│   │      ├── upload.py
│   │      ├── chat.py
│   │      └── ats.py
│   │
│   ├── .env
│   ├── requirements.txt
│   └── venv/
│
├── frontend
│      └── frontend.py
│
├── README.md
│
└── .gitignore
```

---

# 🏗 System Architecture

```
                    User
                      │
                      │
              Upload Resume
                      │
                      ▼
             Streamlit Frontend
                      │
          HTTP Requests (REST API)
                      │
                      ▼
             FastAPI Backend
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Upload Resume      Chat API        ATS API
      │               │                │
      ▼               ▼                ▼
 PDF Extraction     RAG Engine     ATS Engine
      │               │                │
      ▼               ▼                ▼
Sentence          FAISS Search      Groq LLM
Transformer             │
      │                 ▼
      └────────► Relevant Chunks
                         │
                         ▼
                     Groq LLM
                         │
                         ▼
                  AI Generated Response
```

---

# 🎯 Project Objectives

The main objective of HireSense AI is to simplify resume analysis using modern AI technologies.

The project aims to:

- Build an intelligent Resume Assistant.
- Implement Retrieval-Augmented Generation (RAG).
- Perform semantic resume search.
- Improve response accuracy using vector retrieval.
- Compare resumes against Job Descriptions.
- Generate ATS insights automatically.
- Demonstrate practical usage of LLMs in recruitment.

---

# 🔥 Key Highlights

✔ FastAPI Backend

✔ Streamlit Frontend

✔ FAISS Vector Database

✔ Sentence Transformer Embeddings

✔ Groq Llama 3 Integration

✔ Semantic Resume Search

✔ ATS Resume Analysis

✔ Prompt Engineering

✔ Context-aware AI Responses

✔ Modular Code Structure


# ⚙️ How HireSense AI Works

HireSense AI consists of two major AI modules:

1. **Resume Chat (RAG Pipeline)**
2. **ATS Resume Analysis**

Although both modules use the same uploaded resume, they work differently.

---

# 📄 Module 1 — Resume Intelligence (RAG Pipeline)

The Resume Intelligence module enables users to ask natural language questions about their resumes.

Example Questions:

- What projects have I built?
- What are my technical skills?
- Summarize my resume.
- Which programming languages do I know?
- Tell me about my internships.
- What leadership positions have I held?

Instead of sending the entire resume to the LLM, the system first retrieves only the most relevant sections of the resume and then generates the answer.

This architecture is known as **Retrieval-Augmented Generation (RAG).**

---

# 🔄 Resume Upload Workflow

When the user uploads a resume, the following operations occur:

```
User Uploads Resume
        │
        ▼
FastAPI Upload Endpoint
        │
        ▼
Save PDF
        │
        ▼
Extract Text using PyMuPDF
        │
        ▼
Chunk Resume into Small Sections
        │
        ▼
Generate Vector Embeddings
        │
        ▼
Store Embeddings in FAISS
        │
        ▼
Resume Ready for Semantic Search
```

---

# 📑 Step 1 — Resume Upload

The user uploads a PDF resume through the Streamlit interface.

Example:

```
Nitin_Gupta_Resume.pdf
```

The frontend sends the PDF to the FastAPI backend using a POST request.

```
POST /upload-resume
```

---

# 📑 Step 2 — PDF Text Extraction

The uploaded PDF is processed using **PyMuPDF (fitz)**.

The application extracts text from every page.

Example:

```
Resume.pdf

↓

Education

Projects

Experience

Skills

Achievements
```

Now the resume exists as plain text.

---

# 📑 Step 3 — Text Chunking

Instead of embedding the entire resume as one large document, it is divided into multiple smaller chunks.

Example:

```
Chunk 1
Education

------------------

Chunk 2
Projects

------------------

Chunk 3
Experience

------------------

Chunk 4
Skills
```

Chunking improves retrieval accuracy because only the relevant portions of the resume need to be searched.

---

# 📑 Step 4 — Sentence Embeddings

Each chunk is converted into a dense numerical vector using the Sentence Transformer model.

Model Used:

```
all-MiniLM-L6-v2
```

Example:

```
Chunk

↓

"I developed a RAG application."

↓

Embedding

↓

[0.32, -0.17, 0.91, ..., 384 values]
```

Every chunk becomes a **384-dimensional semantic vector**.

Unlike keyword search, embeddings capture the meaning of the text.

---

# 📑 Step 5 — Vector Database (FAISS)

All generated embeddings are stored inside a FAISS vector index.

```
Chunk 1 → Vector 1

Chunk 2 → Vector 2

Chunk 3 → Vector 3

Chunk 4 → Vector 4
```

FAISS allows extremely fast similarity search over these vectors.

---

# 💬 Chat Workflow

Once the resume has been indexed, users can ask questions.

Example:

```
"What projects have I built?"
```

The workflow is:

```
User Question
      │
      ▼
Sentence Transformer
      │
      ▼
Question Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top Relevant Resume Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Groq Llama 3
      │
      ▼
Generated Answer
```

---

# 🔍 Semantic Retrieval

The user question is embedded using the same Sentence Transformer model.

Example:

```
Question

↓

"What projects have I built?"

↓

Embedding

↓

384-dimensional Vector
```

FAISS compares this vector against every stored resume embedding.

Instead of matching words, it matches **meaning**.

The most relevant chunks are returned.

---

# 🧠 Prompt Construction

The retrieved chunks are combined with the user's question.

Example Prompt:

```
You are an AI Resume Assistant.

Use ONLY the context below.

Context:

Projects:
HireSense AI
House Price Prediction

Question:

What projects have I built?
```

Only relevant information is sent to the LLM.

This greatly reduces hallucinations.

---

# 🤖 Response Generation

The prompt is sent to:

```
Groq API

↓

Llama 3.3 70B Versatile
```

The LLM generates a context-aware answer.

Example:

```
You have developed two major projects:

• HireSense AI
• House Price Prediction
```

The answer is returned to the frontend and displayed to the user.

---

# 🎯 Why Use RAG?

Without Retrieval-Augmented Generation:

```
Entire Resume

↓

LLM

↓

Answer
```

Problems:

- Slow
- Expensive
- Higher hallucination risk
- Context window limitations

With RAG:

```
Resume

↓

Semantic Retrieval

↓

Relevant Context

↓

LLM

↓

Answer
```

Benefits:

- Faster
- More accurate
- Lower hallucination
- Lower token usage
- Better scalability

---

# 📊 Module 2 — ATS Resume Analysis

The ATS module compares the uploaded resume with a Job Description.

Unlike Resume Chat, ATS does **not** use FAISS or semantic retrieval.

Instead, it compares the complete resume with the complete JD using prompt engineering.

---

# ATS Workflow

```
Upload Resume
       │
       ▼
Resume Stored
       │
       ▼
Upload Job Description
       │
       ▼
Extract JD Text
       │
       ▼
Prompt Engineering
       │
       ▼
Groq Llama 3
       │
       ▼
Structured JSON Response
       │
       ▼
Frontend Visualization
```

---

# 📄 ATS Processing

The complete resume and complete Job Description are sent to the LLM.

The model is instructed to return structured JSON containing:

- ATS Score
- Matching Skills
- Missing Skills
- Resume Summary
- Improvement Suggestions
- AI-generated Interview Questions

Example Response:

```json
{
  "ats_score": 87,
  "matching_skills": [
    "Python",
    "RAG",
    "FastAPI"
  ],
  "missing_skills": [
    "RLHF",
    "SFT"
  ],
  "summary": "...",
  "suggestions": [
    "...",
    "..."
  ],
  "interview_questions": [
    "...",
    "...",
    "..."
  ]
}
```

---

# 📈 Difference Between Resume Chat and ATS

| Resume Chat | ATS Analysis |
|-------------|--------------|
| Uses RAG | No RAG |
| Uses FAISS | No FAISS |
| Uses Sentence Transformers | No Embeddings |
| Semantic Search | Full Document Comparison |
| Returns Natural Language | Returns Structured JSON |
| Retrieves Context | Compares Resume & JD |

---

# 🎯 Why Separate These Modules?

The Resume Chat module needs semantic retrieval because users ask specific questions.

The ATS module compares two complete documents, so semantic retrieval is unnecessary.

Separating these workflows keeps the architecture modular, efficient, and easier to maintain.


# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/HireSense-AI.git
cd HireSense-AI
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Start the backend:

```bash
python -m uvicorn app:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## 3. Frontend Setup

```bash
cd frontend

python -m streamlit run frontend.py
```

Frontend runs on:

```
http://localhost:8501
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload-resume` | Upload Resume PDF |
| POST | `/chat` | Chat with Resume |
| POST | `/ats` | Analyze Resume against Job Description |

---

# 📁 Important Files

| File | Purpose |
|------|---------|
| `app.py` | FastAPI entry point |
| `utils.py` | PDF extraction, chunking, embeddings, FAISS |
| `rag.py` | Retrieves relevant context and generates answers |
| `llm.py` | Groq LLM integration |
| `ats.py` | ATS analysis logic |
| `routes/upload.py` | Resume upload API |
| `routes/chat.py` | Resume chat API |
| `routes/ats.py` | ATS analysis API |
| `frontend.py` | Streamlit user interface |

---

# 📌 Future Improvements

- Multi-user support
- Persistent FAISS storage
- User authentication
- Chat history
- OCR support for scanned PDFs
- Cloud deployment (Docker + AWS/Azure)
- Hybrid Search (Keyword + Semantic Search)

---

# ⚠ Current Limitations

- Supports one resume at a time
- FAISS index is stored in RAM
- Resume must be uploaded after every backend restart
- ATS analysis depends on LLM reasoning
- Supports PDF resumes only

---

# 🎓 Key Learnings

Through this project I learned:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- FAISS Vector Database
- Sentence Transformers
- Prompt Engineering
- FastAPI Backend Development
- Streamlit UI Development
- REST API Integration
- Groq Llama API Integration

---

---

# 👨‍💻 Author

**Nitin Gupta**

Final Year B.Tech (ECE - IoT)  
Madan Mohan Malaviya University of Technology, Gorakhpur
---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub.