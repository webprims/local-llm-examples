import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

prompt = """
Return ONLY valid JSON for a beginner Python course with these keys:
title, level, duration_weeks, topics.
The topics value must be a JSON array.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "format": "json",
        "stream": False,
    },
    timeout=120,
)
response.raise_for_status()

raw = response.json()["response"]
data = json.loads(raw)

print(json.dumps(data, indent=2))
