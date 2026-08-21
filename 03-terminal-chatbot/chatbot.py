import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

messages = [
    {
        "role": "system",
        "content": "You are a friendly coding tutor. Keep answers clear and practical.",
    }
]

print("Local LLM Chatbot - type 'exit' to stop")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=120,
    )
    response.raise_for_status()

    assistant_message = response.json()["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"AI: {assistant_message}\n")
