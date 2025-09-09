# Graph RAG App

**Graph RAG App** is a full-stack application that allows users to upload files, store metadata, maintain graph relationships, and query an AI-powered knowledge system.

## 🔹 Features

- Upload files to **AWS S3**  
- Store file metadata in **MongoDB**  
- Maintain graph relationships in **Neo4j**  
- AI-powered query system using **vector embeddings** and retrieval-based QA  
- **Asynchronous backend** with FastAPI  
- **Frontend** with React, Tailwind CSS, and Axios  
- CORS enabled for smooth backend-frontend communication  

---

## 🔹 Tech Stack

| Layer       | Technology                       |
|------------ |---------------------------------|
| Backend     | FastAPI (Python)                |
| Frontend    | React + Tailwind CSS + Axios    |
| AI Pipeline | LangChain / Custom embedding + QA chain |
| Database    | MongoDB (metadata) + Neo4j (graph) |
| File Storage| AWS S3                          |
| Async Driver| Motor for MongoDB               |
| Graph Driver| Neo4j official Python driver    |

---

## 🔹 Architecture Diagram

```plaintext
            ┌────────────┐
            │  Frontend  │
            │ (React +   │
            │ Tailwind + │
            │  Axios)    │
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

  AI Pipeline (Vector-based QA):
  ┌─────────────────────────┐
  │ Documents from S3       │
  │ ──> Cleaned / Preprocessed
  │ ──> Embedded (Vector Store)
  │ ──> QA Chain / Retrieval
  └─────────────────────────┘
         ▲
         │
     Answers returned
     to Backend → Frontend
