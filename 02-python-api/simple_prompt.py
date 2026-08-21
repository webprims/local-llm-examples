import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",
    "prompt": "Explain Python functions to a beginner in three short points.",
    "stream": False,
}

response = requests.post(OLLAMA_URL, json=payload, timeout=120)
response.raise_for_status()

print(response.json()["response"])
