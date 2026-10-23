# Agentic AI Course

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20examples-009688?logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20applications-1C3C3C)
![LangGraph](https://img.shields.io/badge/LangGraph-agent%20workflows-1C3C3C)

Practical Python examples for learning modern generative AI and agentic application
development. The course starts with core Python programming and prompt engineering,
then progresses through LLM integrations, APIs, RAG pipelines, asynchronous workers,
LangGraph workflows, memory, and voice-enabled applications.

The repository is organized as small, focused examples so each concept can be
read, run, and extended independently.

## Learning path

| Stage | Directory | Topics |
| --- | --- | --- |
| Python foundations | [`hello_world/`](hello_world/) | First model calls and provider integrations |
| Prompt engineering | [`prompts/`](prompts/) | Zero-shot, few-shot, persona, chain-of-thought, and prompt styles |
| Python fundamentals | [`04_conditionals/`](04_conditionals/) | Conditional logic through small practical programs |
| Python fundamentals | [`05_loops/`](05_loops/) | `for` loops, nested iteration, order processing, and `for...else` |
| Tokenization | [`01_tokenization/`](01_tokenization/) | Tokenization concepts and implementation examples |
| Local models and APIs | [`18_section_ollama/`](18_section_ollama/) | Serving a local Ollama model with FastAPI |
| AI agents | [`20_section_AI_Agents/`](20_section_AI_Agents/) | Tool-oriented agent examples, including weather queries |
| Retrieval-augmented generation | [`21_section_RAG/`](21_section_RAG/) | Document loading, indexing, retrieval, and chat |
| Asynchronous RAG | [`22_section_RAG_async/`](22_section_RAG_async/) | FastAPI, Redis, RQ, and background worker processing |
| Multimodal AI | [`23_section_multimodal/`](23_section_multimodal/) | Multimodal model interaction |
| Stateful workflows | [`24_section_langGraph/`](24_section_langGraph/) | Graph-based conversations and checkpoints |
| Memory | [`26_section_mem_agent/`](26_section_mem_agent/) | Agents that retain conversational context |
| Voice applications | [`28_section_voice_agent/`](28_section_voice_agent/) | Speech recognition and voice interaction |

## What you will build

- Small Python programs that make AI concepts easy to understand.
- Prompt-driven applications using multiple model providers.
- FastAPI services for exposing model functionality over HTTP.
- RAG systems that combine documents, embeddings, vector search, and generation.
- Background RAG processing with Redis and RQ.
- Stateful agent workflows using LangGraph checkpoints.
- Applications that experiment with multimodal input, memory, and speech.

## Technology stack

- **Python** for all examples and services
- **FastAPI** and **Uvicorn** for HTTP APIs
- **OpenAI-compatible** and **Google Gemini** client integrations
- **Ollama** for local model serving
- **LangChain** and **LangGraph** for LLM applications and workflows
- **Qdrant** and **sentence-transformers** for vector retrieval
- **Redis** and **RQ** for asynchronous work queues
- **SpeechRecognition** for the voice example

## Prerequisites

- Python 3.11 or newer
- A terminal and a Python editor such as VS Code
- An API key for examples that use a hosted model provider
- Ollama installed and a local model available for the Ollama section
- Docker Desktop for sections that include a `docker-compose.yml`
- Redis for the asynchronous RAG example

Some examples use external services and cannot run fully offline. Review the
source file for the provider, model name, service URL, and required credentials
before starting it.

## Environment setup

From the project directory, create or activate a virtual environment and install
the shared dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The RAG examples also include section-specific dependency files:

```powershell
python -m pip install -r 21_section_RAG\requirements.txt
python -m pip install -r 22_section_RAG_async\requirements.txt
```

Keep credentials in a local `.env` file when an example supports environment
configuration. Do not place API keys directly in source code or commit them to
version control.

## Running examples

Most lessons are standalone scripts. Run one from the project directory with:

```powershell
python .\05_loops\08_for_else.py
```

For FastAPI examples, start the application with Uvicorn from the section
directory. For example:

```powershell
Set-Location .\18_section_ollama
uvicorn server:app --reload
```

Run commands from the example's directory when its imports are local to that
section. Check the file's `main()` function and comments for the expected
inputs, model setup, and service prerequisites.

## Recommended progression

1. Work through [`04_conditionals/`](04_conditionals/) and [`05_loops/`](05_loops/)
   to refresh Python control flow.
2. Explore [`hello_world/`](hello_world/) and [`prompts/`](prompts/) to understand
   model calls and prompt design.
3. Continue with [`01_tokenization/`](01_tokenization/) and the API example in
   [`18_section_ollama/`](18_section_ollama/).
4. Study the agent and RAG sections in sequence.
5. Finish with LangGraph, memory, multimodal, asynchronous, and voice examples.

## Project conventions

- Examples favor clarity and experimentation over production hardening.
- Dependencies are pinned in the available requirements files for repeatable
  local setup.
- Service URLs, model names, and provider-specific settings should be treated as
  configurable for your environment.
- The `.gitignore` excludes virtual environments, generated Python files, local
  environment files, and credentials.

## Security and cost notes

Hosted model APIs may incur usage charges. Use development credentials with
appropriate limits and avoid sending sensitive data to external providers.
Local-model examples still require sufficient memory and model storage.

## License

No license file is currently included. Treat the repository's source as
educational material unless licensing terms are added.
