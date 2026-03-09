# Tiny LLM Text Assistant (LangChain + Ollama)
 
## Overview
 
This project is a simple **text-to-text AI assistant** built using Python.
It allows users to ask questions through the terminal and receive AI-generated responses using a locally running Large Language Model.
 
The assistant uses **LangChain**, **LangGraph**, and **Ollama** to interact with the **TinyLlama model** and generate responses in real time.
 
This project demonstrates how to build a lightweight AI assistant that runs locally without requiring cloud APIs.
 
---
 
## Problem Statement
 
Many AI assistants rely on cloud APIs and internet connectivity. This project demonstrates how to build a **local AI assistant** that can answer user questions directly from the terminal.
 
For example:
 
User Question:
Top 10 places to visit in Hyderabad
 
Assistant Response:
Charminar
Birla Mandir
Golconda Fort
Ramoji Film City
Hussain Sagar Lake
Salar Jung Museum
Nehru Zoological Park
Shilparamam
Chowmahalla Palace
Lumbini Park
 
This shows how a locally hosted LLM can generate useful responses.
 
---
 
## Features
 
* Text-based AI assistant
* Interactive command-line chat interface
* Uses a local LLM (TinyLlama)
* Streaming AI responses
* Runs completely locally
* Built using LangChain and LangGraph
 
---
 
## Technologies Used
 
* Python
* LangChain
* LangGraph
* Ollama
* TinyLlama LLM
 
---
 
## Installation
 
### 1. Clone the repository
 
git clone https://github.com/your-username/your-repository-name.git
 
cd your-repository-name
 
### 2. Create virtual environment
 
python -m venv .venv
 
### 3. Activate virtual environment
 
Mac/Linux
 
source .venv/bin/activate
 
Windows
 
.venv\Scripts\activate
 
### 4. Install dependencies
 
pip install langchain langchain-ollama langgraph
 
### 5. Install Ollama
 
Install Ollama from:
 
https://ollama.com
 
Then pull the TinyLlama model:
 
ollama pull tinyllama
 
---
 
## Running the Application
 
Run the program using:
 
python A_OpenAIAgent.py
 
You will see:
 
🤏 Tiny Ollama Assistant Ready
Type 'quit' to exit
 
Example interaction:
 
You: Top 10 places to visit in Hyderabad
 
Assistant: Charminar, Birla Mandir, Golconda Fort, Ramoji Film City, Hussain Sagar Lake...
 
Type `quit` to exit the assistant.
 
---
 
## Project Structure
 
ai-projects
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
 
---
 
## Example Code Snippet
 
The assistant uses LangChain with Ollama
 
```python
model = ChatOllama(
    model="tinyllama",
    temperature=0
)
```
 
This connects to the TinyLlama model running locally via Ollama.
 
---
 
## Future Improvements
 
* Add a web interface using Streamlit
* Integrate document search using RAG
* Add memory for conversation history
* Support multiple LLM models
* Deploy as a web application
 
---
 
## Author

Rasool Shaik.