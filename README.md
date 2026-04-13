# CS5600 Assignment 2

## Setup

### 1. Install dependencies

```sh
pip install -r requirements.txt

```

### 2. Setup Neo4j Aura

- Create DB in https://console.neo4j.io
- Copy URI, username, password into `.env`

### 3. Install Ollama

Run:

```sh
ollama run llama3
```

### 4. Run Flask backend

```sh
cd backend
python app.py

```

### 5. Open browser

```md
[http://127.0.0.1:5000]
```

## Features

- CRUD for Neo4j
- Natural language → Cypher via LLM
- GraphQL-ready structure

