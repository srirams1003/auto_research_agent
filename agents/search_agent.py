#implementation of the search agent using langchain
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import os
from utils.arxiv_utils import search_papers
from agents.pdf_agent import process_pdf
from agents.summarizer_agent import summarize_text_chunks
from agents.synthesizer_agent import synthesize_summaries


@tool
def arxiv_search(query: str, max_results: int = 5) -> list:
   """
   Searches for academic papers on arXiv.
  
   Args:
       query: The search term for the papers.
       max_results: The maximum number of results to return.
   """
   return list(search_papers(query, max_results=max_results))


def get_research_agent():
   """
    Initializes and returns the LangChain agent for research.
    """
   google_api_key = os.getenv("GEMINI_API_KEY")

   if not google_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

   llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        google_api_key=google_api_key
    )

   tools = [arxiv_search, process_pdf, summarize_text_chunks, synthesize_summaries]
   prompt = ChatPromptTemplate.from_messages(
       [
           ("system", """You are a comprehensive research assistant with access to academic paper search, PDF analysis, summarization, and synthesis tools.

Available tools:
1. arxiv_search: Search for academic papers on arXiv
2. process_pdf: Download and analyze PDF content to answer questions
3. summarize_text_chunks: Summarize text chunks from papers
4. synthesize_summaries: Combine multiple summaries into a cohesive final summary

Research Workflow:
1. Use arxiv_search to find relevant papers for the user's query
2. For each relevant paper, use process_pdf to extract and analyze content
3. Use summarize_text_chunks to create concise summaries of key sections
4. Use synthesize_summaries to combine all summaries into a comprehensive research overview

When the user asks for research on a topic:
- First search for relevant papers
- Then analyze and summarize each paper's key findings
- Finally, synthesize all findings into a comprehensive research summary

Always explain your process and provide well-structured, academic-quality responses."""),
           ("human", "{input}"),
           ("placeholder", "{agent_scratchpad}"),
       ]
   )
   agent = create_tool_calling_agent(llm, tools, prompt)
   agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
   return agent_executor
