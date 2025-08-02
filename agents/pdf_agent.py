from langchain.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
import tempfile
import requests

@tool
def process_pdf(pdf_url: str, query: str) -> str:
    """
    Downloads a PDF from URL, processes it, and answers questions about it.
    
    Args:
        pdf_url: The URL of the PDF to download and process
        query: The question to ask about the PDF content
    """
    try:
        # Download PDF to temporary file
        response = requests.get(pdf_url)
        response.raise_for_status()
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            tmp_file.write(response.content)
            pdf_path = tmp_file.name
        
        # Load and process PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        # Get API key
        google_api_key = os.getenv("GEMINI_API_KEY")
        if not google_api_key:
            return "Error: GEMINI_API_KEY environment variable not set."
        
        # Initialize LLM and embeddings
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            google_api_key=google_api_key
        )
        embeddings = GoogleGenerativeAIEmbeddings(
            model="embedding-001",
            google_api_key=google_api_key
        )
        
        # Create vector store and QA chain
        vectorstore = FAISS.from_documents(documents, embeddings)
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, 
            retriever=retriever
        )
        
        # Get answer
        result = qa_chain.run(query)
        
        # Clean up temporary file
        os.unlink(pdf_path)
        
        return result
        
    except Exception as e:
        return f"Error processing PDF: {str(e)}" 