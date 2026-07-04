# test_embedding.py

import requests

r = requests.post(
    "http://localhost:11434/api/embeddings",
    json={
        "model": "nomic-embed-text",
        "prompt": "hello world"
    }
)

data = r.json()

print(type(data["embedding"]))
print(len(data["embedding"]))