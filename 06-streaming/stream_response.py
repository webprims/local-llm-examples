import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

with requests.post(
    OLLAMA_URL,
    json={
        "model": "llama3.2",
        "prompt": "Explain what an API is in simple terms.",
        "stream": True,
    },
    stream=True,
    timeout=120,
) as response:
    response.raise_for_status()

    for line in response.iter_lines():
        if not line:
            continue

        chunk = json.loads(line.decode("utf-8"))
        print(chunk.get("response", ""), end="", flush=True)

print()
