# 🤖 AI Research Agent

An autonomous AI research agent that can answer questions and search the web in real-time. Built with LangGraph, Ollama, and Tavily Search.

## 🚀 What it does

- Answers questions using AI
- Automatically searches the web when it needs current information
- Decides by itself when to search vs when to answer directly
- Clean chat interface built with Streamlit
- Safety guardrails — refuses harmful or 18+ content

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| LangGraph | Agent framework and decision making |
| Ollama (llama3.1) | Local LLM brain |
| Tavily Search | Real-time web search |
| Streamlit | Chat UI |
| LangChain | LLM orchestration |

## ⚙️ How to run locally

1. Clone the repo
2. Install dependencies:
pip install -r requirements.txt
3. Install Ollama from ollama.com and pull the model:
ollama pull llama3.1
4. Create a `.env` file:
TAVILY_API_KEY=your_tavily_key_here
5. Run the app:
streamlit run app.py

## 🔮 Planned upgrades

- Switch to OpenAI GPT for faster responses (deployment)
- Add image generation
- Add memory across sessions
- Add document upload and analysis

## Status
Active development 🚀

## 👨‍💻 Author

Sriharsha Koppula 