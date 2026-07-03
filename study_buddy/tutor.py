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
            timeout=180
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]

    except Exception as e:
        return f"Error talking to Ollama: {str(e)}"import requests


