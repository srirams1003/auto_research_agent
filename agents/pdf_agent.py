from utils.pdf_utils import download_pdf, extract_chunks
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrivevalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.embeddings import GoogleGenerativeAIEmbeddings

llm = ChatGoogleGenerativeAI(model_name="gemini-1.5-flash", temperature=0)
embeddings = GoogleGenerativeAIEmbeddings()


def pdf_agent(document, query):
    loader = PyPDFLoader(document)  #Initializes the pdf loader for a specific document
    documents = loader.load()  #Loads the document into a list of document objects 
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-gecko-001")
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrivevalQA.from_chain_type(llm = ChatGoogleGenerativeAI(model = "gemini-pro"), retriever=retriever)
    result =  qa_chain.run(query)
    print(result)
    





#def pdf_agent(paper):
#    pdf_url = paper.pdf_url
#    filename = pdf_url.split("/")[-1]
#    download_pdf(pdf_url, f"/tmp/{filename}")
#    chunks = extract_chunks(f"/tmp/{filename}")
 #   return chunks 