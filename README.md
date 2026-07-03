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
