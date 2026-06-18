# RAG Document Q&A System

## Features

- PDF ingestion
- Vector search using FAISS
- Hugging Face LLM integration
- FastAPI backend
- Streamlit frontend
- Query analytics

## Tech Stack

- Python
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- Hugging Face
- SQLite

## Run Backend

python -m uvicorn backend.main:app --reload

## Run Frontend

streamlit run frontend/app.py

## API Endpoints

POST /ingest
POST /ask
GET /analytics

<!-- -----For Biginer Users------------->

# 📄 RAG Document Q&A System

A Retrieval-Augmented Generation (RAG) based Document Question Answering System built using FastAPI, Streamlit, FAISS, Sentence Transformers, and Hugging Face Inference API.

The system allows users to ask questions about a PDF document (AWS Customer Agreement) and receive context-aware answers generated using an LLM.

---

# 🚀 Features

- PDF Document Ingestion
- Automatic Text Chunking
- Vector Embeddings Generation
- FAISS Vector Database
- Semantic Search
- LLM-based Answer Generation
- Query Logging
- Analytics Dashboard
- FastAPI Backend
- Streamlit Frontend

---

# 🏗️ System Architecture

```text
PDF Document
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Retrieved Context
      │
      ▼
Hugging Face LLM
      │
      ▼
Generated Answer
      │
      ▼
User Interface
```

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Python
- SQLAlchemy
- SQLite

## RAG Components

- LangChain
- FAISS
- Sentence Transformers
- Hugging Face Inference API

## Frontend

- Streamlit

## Database

- SQLite

---

# 📂 Project Structure

```text
rag-document-qa/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   ├── database.py
│   ├── models.py
│   ├── analytics.py
│   └── aws_customer_agreement.pdf
│
├── frontend/
│   └── app.py
│
├── database/
│   └── logs.db
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone <repository-url>
cd rag-document-qa
```

---

## Step 2: Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate Environment

```bash
.venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Hugging Face Setup

## Create Account

Visit:

```text
https://huggingface.co
```

Create a free account.

---

## Generate Token

Open:

```text
https://huggingface.co/settings/tokens
```

Create a token with:

```text
Role: Read
```

Copy the token.

Example:

```text
hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Configure Token

Open:

```python
backend/rag.py
```

Replace:

```python
token="YOUR_HF_TOKEN"
```

with:

```python
token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

# 📥 PDF Ingestion

Place the PDF file inside:

```text
backend/
```

Rename:

```text
AWS Customer Agreement.pdf
```

to

```text
aws_customer_agreement.pdf
```

---

# ▶️ Running the Backend

Start FastAPI:

```bash
python -m uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📚 Ingesting the Document

Open:

```text
http://127.0.0.1:8000/docs
```

Select:

```text
POST /ingest
```

Click:

```text
Try it out
```

Then:

```text
Execute
```

Expected Response:

```json
{
  "chunks_created": 32
}
```

---

# ❓ Asking Questions

Open:

```text
POST /ask
```

Request:

```json
{
  "query": "Can AWS access my content?"
}
```

Response:

```json
{
  "answer": "...",
  "sources": [
    "...",
    "..."
  ]
}
```

---

# 📊 Analytics

Endpoint:

```text
GET /analytics
```

Returns:

- Most Asked Questions
- Average Response Time
- Unanswered Queries

Example:

```json
{
  "top_questions": [
    {
      "question": "Can AWS access my content?",
      "count": 3
    }
  ],
  "avg_latency": 1.5,
  "no_answer_queries": []
}
```

---

# 🖥️ Running the Frontend

Open another terminal.

Activate virtual environment:

```bash
.venv\Scripts\activate
```

Run:

```bash
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🔍 Sample Questions

## Relevant Questions

```text
Can AWS access my content?
What is AWS liability limit?
Can AWS terminate my account?
What is the payment policy?
What are customer responsibilities?
```

## Irrelevant Questions

```text
Who won IPL 2025?
What is Python?
Who is Elon Musk?
```

---

# 📈 RAG Configuration

| Parameter | Value |
|------------|---------|
| Chunk Size | 1000 |
| Chunk Overlap | 200 |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Store | FAISS |
| Top K Retrieval | 3 |
| LLM | Llama 3.1 / Hugging Face |
| Database | SQLite |

---

# 🗄️ Database Logging

Every query is stored with:

- Question
- Generated Answer
- Source Context
- Response Time
- Answer Found Status
- Timestamp

Database Location:

```text
database/logs.db
```

---

# 📌 API Endpoints

## Ingest Document

```http
POST /ingest
```

---

## Ask Question

```http
POST /ask
```

Request:

```json
{
  "query": "Question here"
}
```

---

## Analytics

```http
GET /analytics
```

---

# 🔮 Future Improvements

- Multi-document support
- PDF Upload from UI
- User Authentication
- Conversation Memory
- Source Citations with Page Numbers
- Analytics Charts
- Docker Deployment
- Cloud Deployment (AWS/Azure)

---

# 👨‍💻 Author

Developed as part of the Junior AI Developer Technical Assignment.

Technologies Used:

- Python
- FastAPI
- Streamlit
- LangChain
- FAISS
- Hugging Face
- SQLite
