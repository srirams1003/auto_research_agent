# from utils.arxiv_utils import search_papers

# print("test line")

# def search_agent(query, max_results=5):
#     return list(search_papers(query, max_results=max_results)) 



#implementation of the search agent using langchain
from langchain.tools import tool 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
import os
from utils.arxiv_utils import search_papers

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
    if "GEMINI_API_KEY" not in os.environ:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0) # Use the appropriate Gemini model name

    tools = [arxiv_search]
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful research assistant. You have access to a tool for searching academic papers."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor