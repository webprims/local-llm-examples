import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

messages = [
    {
        "role": "system",
        "content": "You are a concise coding tutor. Explain concepts with practical examples.",
    }
]

print("Local chat with memory. Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False,
        },
        timeout=120,
    )
    response.raise_for_status()

    answer = response.json()["message"]["content"].strip()
    messages.append({"role": "assistant", "content": answer})

    print(f"Assistant: {answer}")
