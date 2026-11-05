# Multi-Agent Web & Finance Assistant

A lightweight multi-agent backend built with [Agno](https://github.com/agno-agi/agno) and served via AgentOS. It runs a web search agent and a financial analyst agent side-by-side using Groq for fast inference.

## What it does

- **Web Search Agent**: Searches DuckDuckGo for up-to-date information and cites sources.
- **Finance Agent**: Uses Yahoo Finance to fetch stock prices, analyst recommendations, company fundamentals, and corporate news, formatted in tables.
- **AgentOS**: Exposes both agents via a local FastAPI app with live reloading.

## Prerequisites

- Python 3.10+
- A [Groq API key](https://console.groq.com/)

## Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Latikesh22/Financial-agent.git
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Add your API key**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Make sure your script is named `agno_assist.py`:

```bash
python agno_assist.py
```

AgentOS will serve the app locally with hot reload enabled.

## Example Prompts

- **Finance**: *"Compare the P/E ratios and analyst recommendations for NVDA and AMD."*
- **Search**: *"What are the key takeaways from the latest Federal Reserve meeting? Include sources."*