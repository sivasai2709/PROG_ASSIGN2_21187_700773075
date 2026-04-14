import requests
from config import OLLAMA_URL, OLLAMA_MODEL

def natural_to_cypher(user_input):
    prompt = f"""
You are a Neo4j Cypher expert.

Convert the user request into ONLY a Cypher query.

Schema:
Node Labels:
- Characters(name, height, mass, gender, homeworld)
- Species(name, classification, language)
- Planets(name, climate, population)

Relationships:
- FROM
- IDENTIFIES_AS
- ORIGINATED_FROM

Rules:
- Return ONLY Cypher, no explanation.
- Ensure correctness.

User request:
{user_input}
"""

    response = requests.post(OLLAMA_URL, json={
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"].strip()