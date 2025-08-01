from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os


#summarizes text chunks using the Gemini LLM
@tool
def summarize_text_chunks(text_chunks: str) -> str:
    
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
        
        # Split into chunks if multiple are provided
        chunks = text_chunks.split('\n\n')
        summaries = []
        
        # Summarize each chunk (limit to first 2 chunks like original)
        for chunk in chunks[:2]:
            if chunk.strip():
                prompt = f"You are a helpful summarizer. Please provide a concise summary of the following text:\n\n{chunk}"
                response = llm.invoke(prompt)
                summaries.append(response.content.strip())
        
        return "\n\n".join(summaries)
        
    except Exception as e:
        return f"Error summarizing text: {str(e)}"  