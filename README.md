# CogneeTest

A testing and experimentation repository for building AI memory systems with Cognee.

This project validates both local and cloud-based memory pipelines, allowing the same application logic to run either completely offline using Ollama or through Cognee Cloud for faster performance.

## What This Repository Demonstrates

* AI memory using Cognee
* Knowledge graph creation from natural language
* Entity and relationship extraction
* Vector embeddings and semantic retrieval
* Local-first AI infrastructure
* Cloud and local backend switching with minimal code changes

## Architecture

### Cloud Mode

* Cognee Cloud
* Managed memory infrastructure
* Fast setup and reliable performance
* Uses hackathon-provided credits

### Local Mode

* Ollama
* qwen2.5:7b for entity extraction
* nomic-embed-text for embeddings
* LanceDB for vector storage
* Zero API cost

The same codebase supports both modes through configuration changes.

## Tech Stack

* Python
* Cognee
* Ollama
* qwen2.5:7b
* nomic-embed-text
* LanceDB

## Project Structure

```text
.
├── test.py
├── test_cloud.py
├── test_unified.py
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rajtiwari0202/CogneeTest.git
cd CogneeTest
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment Variables

Create a `.env` file:

```env
COGNEE_CLOUD_API_KEY=your_api_key
```

## Running Locally

Start Ollama:

```bash
ollama serve
```

Pull required models:

```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

Run the unified test:

```bash
python test_unified.py
```

## What Was Validated

During development the following issues were identified and resolved:

* Missing API key configuration
* Missing embedding dimensions
* Tokenizer configuration issues
* Incorrect Ollama embedding endpoint usage
* Model compatibility issues for structured extraction

After debugging, the complete memory pipeline successfully performs:

1. Text ingestion
2. Entity extraction
3. Relationship generation
4. Embedding creation
5. Vector storage
6. Semantic retrieval

## Sample Result

Input:

```text
The testing involves testing an automation script in local mode.
```

Retrieved Memory:

```text
The testing involves testing an automation script in local mode.
```

This confirms successful ingestion, storage, indexing, and retrieval across the memory pipeline.

## Hackathon Context

Built during **The Hangover Part AI Hackathon** hosted by WeMakeDevs and powered by Cognee.

Goal: Explore practical AI memory systems that can retain, organize, and retrieve information across interactions rather than starting every session from scratch.

## Future Plans

* Adaptive Study Tutor
* Persistent learning history
* Quiz generation from memory
* Personalized revision tracking
* Long-term conversational memory
