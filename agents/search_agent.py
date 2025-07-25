from utils.arxiv_utils import search_papers

print("test line")

def search_agent(query, max_results=5):
    return list(search_papers(query, max_results=max_results)) 
