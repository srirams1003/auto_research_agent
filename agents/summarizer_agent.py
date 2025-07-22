from utils.llm_utils import summarize_text

def summarizer_agent(chunks):
    return [summarize_text(chunk) for chunk in chunks[:3]]  # Summarize first 3 chunks 