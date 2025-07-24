import arxiv

def search_papers(query, max_results=5):
    return arxiv.Search(query=query, max_results=max_results) 