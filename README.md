# README

## Introduction

This project utilizes `ollama`, `langchain`, and `chromadb` to analyze a codebase, create documents, generate vector embeddings, and query a vector store based on user input prompts.

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package manager)
- Required Python libraries:
  - `ollama`
  - `langchain`
  - `chromadb`
  - `pytest`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # For Windows: env\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install ollama langchain chromadb pytest
    ```
    or
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Adjust the `excluded_dirs` and `codebase_root_dir` variables in the script according to your setup:

```python
excluded_dirs = ["node_modules", "dist", ".idea"]
codebase_root_dir = "/path/to/your/codebase"
```

## Usage

```python
python3 main.py
```

## Functionnality

- Reading the codebase:
	•	Utilizes read_codebase to read file contents from the specified directory, excluding designated directories.
- Creating documents:
	•	Generates Document objects for each file with content and appropriate metadata.
- Initializing ChromaDB:
	•	Sets up a ChromaDB client and creates a collection to store documents and their embeddings.
- Generating embeddings:
	•	Computes vector embeddings for each document using the nomic-embed-text model from ollama.
- Querying the vector store:
	•	Allows interactive querying by prompting users. Embeddings are generated for prompts and used to query the vector store, producing responses via the llama3 model.

Example output :

```bash
Creating documents...
Creating vector store...
Please enter your prompt (or type 'exit' to quit): What is the purpose of this codebase?
Retrieve document for prompt...
README
Generate response...
This script is designed to...
```

## Running tests

```bash
cd test
pytest
```

## Improvements

- Persistent ChromaDB Storage: Save ChromaDB data to avoid regeneration on each run.
- Enhanced Embedding Phase: Improve embedding process for more precise responses.
- Chat History
- ...
