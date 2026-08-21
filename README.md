# Local LLM Examples

Practical examples for running and integrating local language models with **Ollama** and Python.

This repository is maintained by **WebPrims** for students and developers who want to understand local AI workflows without depending entirely on hosted APIs.

## What you'll learn

- Installing and using Ollama
- Running open-weight models locally
- Calling a local model from Python
- Building a simple terminal chatbot
- Sending system and user prompts
- Using structured JSON-style outputs
- Streaming model responses
- Keeping AI experiments private and local

## Repository structure

```text
local-llm-examples/
├── 01-ollama-basics/
├── 02-python-api/
├── 03-terminal-chatbot/
├── 04-system-prompts/
├── 05-structured-output/
├── 06-streaming/
└── requirements.txt
```

## Requirements

- Python 3.10+
- Ollama installed locally
- A downloaded model such as `llama3.2`

Install Ollama from its official website, then pull a model:

```bash
ollama pull llama3.2
```

Test it:

```bash
ollama run llama3.2
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Learning approach

Start with the command-line examples first. Once you understand how a model runs locally, move to the Python API examples and then build the chatbot and structured-output examples.

Try changing models, prompts, temperatures, and response formats. The goal is to understand the workflow rather than just copy code.

## Why local LLMs?

Local models can be useful when you want more control over privacy, cost, experimentation, latency, or self-hosted AI workflows. They are also a good way to learn how modern AI applications work under the hood.

## Learn AI with WebPrims

WebPrims focuses on practical, project-driven training in AI, local/open-weight models, software development and modern coding workflows.

- AI Edge: https://www.webprims.com/ai-edge
- Official Website: https://www.webprims.com/
- GitHub: https://github.com/webprims

## License

This repository is provided for learning and educational use by WebPrims.
