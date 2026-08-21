import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

messages = [
    {
        "role": "system",
        "content": "You are a patient Python tutor. Use simple language and one small example.",
    },
    {
        "role": "user",
        "content": "What is a Python dictionary?",
    },
]

response = requests.post(
    OLLAMA_URL,
    json={"model": "llama3.2", "messages": messages, "stream": False},
    timeout=120,
)
response.raise_for_status()

print(response.json()["message"]["content"])
