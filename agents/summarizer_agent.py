from utils.llm_utils import summarize_text

def summarizer_agent(chunks):
    # TODO: For now, only summarize first 2 chunks. Hopefully the first 2 chunks are enough to get the abstract of the paper.
    return [summarize_text(chunk) for chunk in chunks[:2]]  