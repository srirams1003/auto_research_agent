from agents.search_agent import search_agent
from agents.pdf_agent import pdf_agent
from agents.summarizer_agent import summarizer_agent
from agents.synthesizer_agent import synthesizer_agent

def main():
    query = input("Enter research query: ")
    papers = search_agent(query)
    all_summaries = []
    for paper in papers:
        print(f"🔍 Processing paper: {paper.title}")
        chunks = pdf_agent(paper)
        summaries = summarizer_agent(chunks)
        all_summaries.extend(summaries)
    final = synthesizer_agent(all_summaries)
    print("\n=== 🧠 Synthesized Summary ===\n")
    print(final)

if __name__ == "__main__":
    main() 