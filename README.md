# AI Flight Orchestrator

Version from 31/05/2026

AI Flight Orchestrator is a Python-based Retrieval-Augmented Generation (RAG) system designed for airport search and intelligent question answering.

The project combines:

* FastAPI REST API
* FAISS vector database
* HuggingFace embeddings
* Mistral LLM
* LangChain integration

The system allows semantic airport search and natural language question answering based on airport metadata.

---

# Architecture

```text
User
  |
  v
FastAPI Endpoint
  |
  v
RAG Resolver
  |
  +------> FAISS Retriever
  |             |
  |             v
  |       Airport Documents
  |
  v
Mistral LLM
  |
  v
Final Answer
```

---

# Project Structure

```text
ai-flight-orchestrator/
│
├── api/
│   ├── main.py
│   ├── faiss_endpoint.py
│   └── rag_endpoint.py
│
├── orchestration/
│   ├── FAISS_resolver.py
│   └── RAG_resolver.py
│
├── retrieval/
│   └── airport_FAISS.py
│
├── providers/
│   ├── base.py
│   └── mistral_provider.py
│
├── data/
│   ├── airports.csv
│   └── faiss_airports/
│
├── tests/
│   └── mistral_response.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# Features

## 1. Airport Vector Search

Airport data is loaded from:

```text
data/airports.csv
```

Each airport is converted into a LangChain Document:

```python
Document(
    page_content=text,
    metadata=row.to_dict()
)
```

Example document:

```text
Airport: Frederic Chopin Airport
City: Warsaw
Country: PL
ICAO: EPWA
IATA: WAW
```

---

## 2. Embeddings

Embeddings are generated using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

through:

```python
HuggingFaceEmbeddings
```

Example:

```python
self.embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

## 3. FAISS Vector Store

The first application startup creates a FAISS index.

```text
data/faiss_airports/
```

Subsequent startups load the existing index.

Example startup log:

```text
Loaded 9803 airports from CSV
Loading existing FAISS index...
FAISS ready in 8.6 seconds
```

---

## 4. Semantic Airport Search

Example request:

```http
GET /FAISSsearch?query=Lublin
```

Example response:

```json
[
  {
    "code": "LUZ",
    "icao": "EPLB",
    "name": "Lublin Airport",
    "country": "PL"
  }
]
```

The search uses:

```python
similarity_search()
```

from FAISS.

---

# Retrieval Layer

## AirportFAISS

Responsible for:

* loading CSV
* generating embeddings
* loading/saving FAISS
* semantic search

Main method:

```python
search(
    query: str,
    k: int = 5
)
```

Returns:

```python
List[Document]
```

---

# Orchestration Layer

## FAISS Resolver

Simple retrieval wrapper.

```python
resolver.resolve(
    query="Warsaw",
    k=5
)
```

Returns retrieved documents.

---

## RAG Resolver

Combines retrieval with LLM generation.

```python
docs = self.faiss_repository.search(
    query=query,
    k=5
)
```

Creates context:

```python
context = "\n".join(
    doc.page_content
    for doc in docs
)
```

Builds prompt:

```python
Question:
{query}

Context:
{context}
```

and sends it to the language model.

---

# Mistral Integration

## Environment Variable

Create:

```text
.env
```

```env
MISTRAL_API_KEY=YOUR_KEY
```

---

## Provider

```python
provider = MistralProvider()
```

Uses:

```python
mistral-large-latest
```

Example:

```python
response = self.client.chat.complete(
    model="mistral-large-latest",
    messages=messages
)
```

---

# API Endpoints

## FAISS Search

```http
GET /FAISSsearch
```

Parameters:

```text
query
k
```

Example:

```http
GET /FAISSsearch?query=Lublin&k=4
```

---

## RAG Search

```http
GET /RAGsearch
```

Parameters:

```text
query
```

Example:

```http
GET /RAGsearch?query=famous pianist
```

Example response:

```json
{
  "query": "famous pianist",
  "answer": {
    "answer": "Frederic Chopin Airport is named after the famous Polish composer and pianist Frederic Chopin.",
    "sources": [...]
  }
}
```

---

# Running the Project

## Create virtual environment

```bash
python -m venv env311
```

Activate:

```bash
env311\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

```bash
uvicorn api.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Example Queries

## Airport search

```text
Lublin
```

```text
Warsaw
```

```text
London airport
```

```text
airport in Austria
```

---

## RAG search

```text
famous pianist
```

```text
airport named after composer
```

```text
airport named after musician
```

```text
airport related to Chopin
```

```text
airport named after historical figure
```

---

# Future Improvements

## Dynamic Retrieval

Instead of fixed:

```python
k=5
```

use adaptive retrieval based on similarity score.

---

## Metadata Filtering

Examples:

```text
country = PL
```

```text
type = AP
```

---

## Hybrid Search

Combine:

* vector search
* keyword search

for higher accuracy.

---

## Cross Encoder Re-ranking

Improve retrieval quality with:

```text
bge-reranker-large
```

or

```text
ms-marco-MiniLM
```

---

## Conversation Memory

Add:

```text
LangChain Memory
```

or

```text
LangGraph
```

to support multi-turn conversations.

---

## Flight Data Integration

Future extension:

```text
ADS-B
OpenSky
FlightRadar
```

allowing real-time flight intelligence.

---

# Technologies

* Python 3.11
* FastAPI
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers
* Mistral AI
* Uvicorn
* Pandas

---

# Author

Bartłomiej Bielecki


Project developed as an experimentation platform for:

* Vector Databases
* Retrieval-Augmented Generation
* LLM Orchestration
* FastAPI Services
* AI Engineering
