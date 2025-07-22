from utils.llm_utils import summarize_text

def synthesizer_agent(summaries):
    combined = "\n\n".join(summaries)
    prompt = f"Here are individual summaries:\n\n{combined}\n\nWrite a cohesive, unified summary."
    return summarize_text(prompt) 