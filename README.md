<img width="919" height="774" alt="image" src="https://github.com/user-attachments/assets/a8bd5688-9c1d-40fb-9020-55625512e99e" />





# Bangladesh AI Agent
An intelligent AI-powered assistant that answers questions about Bangladesh — hospitals, educational institutions, restaurants, and general knowledge — using LangChain, Groq LLM, SQLite databases, and a FastAPI web interface.

---

## Project Structure

bangladesh-ai-agent/
|
|-- agent/                        # Core AI Agent logic
|   |-- main_agent.py             # LangChain ReAct Agent setup
|   |-- llm.py                    # Groq LLM configuration
|   └-- prompts.py                # Agent prompt templates
|
|-- app/                          # FastAPI Web Application
|   |-- __init__.py
|   |-- main.py                   # FastAPI routes (GET /, POST /ask)
|   └-- agent_runner.py           # Bridge between FastAPI and LangChain agent
|
|-- tools/                        # LangChain Tools
|   |-- hospital_tool.py          # Query hospitals from SQLite DB
|   |-- institution_tool.py       # Query educational institutions from SQLite DB
|   |-- restaurant_tool.py        # Query restaurants from SQLite DB
|   └-- web_search.py             # Web search tool for general knowledge
|
|-- databases/                    # SQLite Databases
|   |-- hospitals.db
|   |-- institutions.db
|   └-- restaurants.db
|
|-- data/                         # Raw CSV source data
|   |-- hospitals.csv
|   |-- institutions.csv
|   └-- restaurants.csv
|
|-- utils/                        # Utility helpers
|   └-- db_helper.py              # SQLite query executor
|
|-- templates/                    # HTML Frontend
|   └-- index.html                # Chat UI
|
|-- static/                       # Static Assets
|   └-- style.css
|
|-- .env                          # Environment variables (not committed)
|-- .gitignore
|-- requirements.txt
└-- README.md

---

## How It Works

User Question
     |
     v
FastAPI /ask endpoint
     |
     v
LangChain ReAct Agent (Groq LLM - llama-3.3-70b-versatile)
     |
     |---> hospital_tool     -> SQL query on hospitals.db
     |---> institution_tool  -> SQL query on institutions.db
     |---> restaurant_tool   -> SQL query on restaurants.db
     └---> web_search        -> General knowledge questions
     |
     v
Answer returned to UI

---

## Tech Stack

Layer                | Technology
---------------------|---------------------------
LLM                  | Groq API (llama-3.3-70b-versatile)
Agent Framework      | LangChain ReAct Agent
Backend              | FastAPI + Uvicorn
Database             | SQLite3
Frontend             | HTML + CSS + Vanilla JS
Templating           | Jinja2
Environment          | Python 3.11

---

## Setup and Installation

1. Clone the repository

git clone https://github.com/Ekaanta/Learn-Bangladesh-AI-Agent.git
cd Learn-Bangladesh-AI-Agent

2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

GROQ_API_KEY=your_groq_api_key_here

Get your free API key at: https://console.groq.com

5. Run the application

uvicorn app.main:app --reload

6. Open in browser

http://127.0.0.1:8000

---

## Example Questions

- Best hospitals in Dhaka?
- List universities in Sylhet division
- Top rated restaurants in Chittagong?
- How many private hospitals are in Rajshahi?
- Who is the founder of Bangladesh?

---

## Environment Variables

Variable        | Description
----------------|------------------------------------------
GROQ_API_KEY    | Your Groq API key from console.groq.com

---

## Author

Ekanta Banik Durjoy
GitHub: https://github.com/Ekaanta

---

## License

This project is open source and available under the MIT License.
