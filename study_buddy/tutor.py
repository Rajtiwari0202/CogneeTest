# study_buddy/tutor.py

import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(prompt: str) -> str:
    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "qwen2.5:7b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Sorry, I could not generate a response."
        )

    except Exception as e:
        return f"LLM Error: {str(e)}"