import arxiv

def search_papers(query, max_results=5):
    # Construct the default API client.
    client = arxiv.Client()
    # search = arxiv.Search(query=query, max_results=max_results, sort_by = arxiv.SortCriterion.SubmittedDate) 
    search = arxiv.Search(query=query, max_results=max_results) 
    results = client.results(search)

    return results