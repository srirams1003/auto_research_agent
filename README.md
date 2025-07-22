# Auto Research Agent

A lightweight agentic AI tool to search, summarize, and synthesize research papers from arXiv or Semantic Scholar.

## Features
- Search for relevant papers
- Download and chunk PDFs
- Summarize papers using LLMs
- Synthesize unified answers

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```
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