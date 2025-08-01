from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

@tool
def synthesize_summaries(summaries: str) -> str:
    """
    Combines multiple summaries into a cohesive, unified final summary.
    
    Args:
        summaries: Multiple summaries separated by newlines to be combined
    """
    try:
        # Get API key
        google_api_key = os.getenv("GEMINI_API_KEY")
        if not google_api_key:
            return "Error: GEMINI_API_KEY environment variable not set."
        
        # Initialize LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            google_api_key=google_api_key
        )
        
        prompt = f"""You are a research synthesis expert. Here are individual summaries from multiple sources:

{summaries}

Please write a cohesive, unified summary that:
1. Identifies common themes and patterns
2. Highlights key findings and insights
3. Provides a comprehensive overview of the research landscape
4. Maintains academic rigor and clarity

Write a well-structured final summary:"""
        
        response = llm.invoke(prompt)
        return response.content.strip()
        
    except Exception as e:
        return f"Error synthesizing summaries: {str(e)}" 