# Auto Research Agent

Look at github-instructions.md to see how to make changes

A lightweight agentic AI tool to search, summarize, and synthesize research papers from arXiv or Semantic Scholar.

## Features
- Search for relevant papers
- Download and chunk PDFs
- Summarize papers using LLMs
- Synthesize unified answers

## Quickstart

0. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # macOS/Linux
    ```
    <!-- .venv\Scripts\activate      # Windows -->

    ##### NOTE: You have to run the `source .venv/bin/activate` command every time you open a new terminal for this project.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your environment

    Copy the .env.example file to .env and add your Gemini API Key:

    ```python
    cp .env.example .env
    ```

    Inside .env:

    ```
    GEMINI_API_KEY=your-gemini-api-key-here
    ```

    [ 🔑 ] Get your Gemini API key from: https://makersuite.google.com/app/apikey

3. Run the main program:
   ```bash
   python main.py
   ```

## Project Structure

```
auto_research_agent/
├── agents/
│   ├── search_agent.py
│   ├── pdf_agent.py
│   ├── summarizer_agent.py
│   └── synthesizer_agent.py
├── utils/
│   ├── arxiv_utils.py
│   ├── pdf_utils.py
│   └── llm_utils.py
├── main.py
├── requirements.txt
└── README.md
``` 
