#implementation of the search agent using langchain
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import os
from utils.arxiv_utils import search_papers
from agents.pdf_agent import process_pdf


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

   tools = [arxiv_search, process_pdf]
   prompt = ChatPromptTemplate.from_messages(
       [
           ("system", """You are a helpful research assistant with access to academic paper search and PDF analysis tools.

Available tools:
1. arxiv_search: Search for academic papers on arXiv
2. process_pdf: Download and analyze PDF content to answer questions

Workflow:
1. Use arxiv_search to find relevant papers for the user's query
2. For each relevant paper, use process_pdf to analyze its content and answer specific questions
3. Provide comprehensive research insights based on the papers found

Always explain what you're doing and provide clear, well-structured responses."""),
           ("human", "{input}"),
           ("placeholder", "{agent_scratchpad}"),
       ]
   )
   agent = create_tool_calling_agent(llm, tools, prompt)
   agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
   return agent_executor
