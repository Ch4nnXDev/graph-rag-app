# AI Agent API

AI Agent API is a FastAPI-based backend that allows uploading files to S3, storing file metadata in MongoDB, maintaining relationships in Neo4j, and querying an AI-powered knowledge system using vector embeddings and a QA chain.

## 🔹 Features

- Upload files to AWS S3
- Store file metadata in **MongoDB**
- Store graph relationships (e.g., file connections, tags) in **Neo4j**
- AI-powered query system using **vector embeddings** and **retrieval-based QA**
- Asynchronous FastAPI backend
- CORS enabled for frontend integration

---

## 🔹 Tech Stack

- **Backend**: FastAPI (Python)
- **AI Pipeline**: LangChain / Custom embedding + QA chain
- **Database**: MongoDB (metadata) + Neo4j (graph relationships)
- **File Storage**: AWS S3
- **Async Driver**: Motor for MongoDB
- **Neo4j Driver**: Official Python driver

---

## 🔹 Architecture Diagram

```plaintext
          ┌────────────┐
          │  Frontend  │
          │ (React/Vue)│
          └─────┬──────┘
                │ HTTP Requests
                ▼
          ┌────────────┐
          │  FastAPI   │
          │  Backend   │
          └─────┬──────┘
      Upload / Query │
          ┌─────────┴─────────┐
          ▼                   ▼
   ┌────────────┐        ┌────────────┐
   │   AWS S3   │        │  MongoDB   │
   │ (File Data)│        │ (Metadata) │
   └────────────┘        └────────────┘
                             │
                             ▼
                         ┌────────────┐
                         │  Neo4j     │
                         │ (Graph)    │
                         └────────────┘

  AI Pipeline:
  ┌───────────────┐
  │ Vector Store  │
  │ + QA Chain    │
  └───────────────┘
         ▲
         │
  Documents loaded from S3 + cleaned + embedded
