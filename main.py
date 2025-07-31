# from agents.search_agent import search_agent
# from agents.pdf_agent import pdf_agent
# from agents.summarizer_agent import summarizer_agent
# from agents.synthesizer_agent import synthesizer_agent


# def main():
#     query = input("Enter research query: ")
#     papers = search_agent(query)
#     all_summaries = []
#     for paper in papers:
#         print(f"🔍 Processing paper: {paper.title}")
#         chunks = pdf_agent(paper)
#         summaries = summarizer_agent(chunks)
#         all_summaries.extend(summaries)
#     final = synthesizer_agent(all_summaries)
#     print("\n=== 🧠 Synthesized Summary ===\n")
#     print(final)


# if __name__ == "__main__":
#     main()


# main.py
import os
from agents.search_agent import get_research_agent
from dotenv import load_dotenv


if __name__ == "__main__":
   # Load environment variables (e.g., from a .env file)
   load_dotenv()


   # Get the agent executor
   agent_executor = get_research_agent()


   # Example usage
   print("Agent is ready. How can I help you with your research?")


   while True:
       try:
           user_input = input("> ")
           if user_input.lower() in ["exit", "quit"]:
               break
          
           response = agent_executor.invoke({"input": user_input})
           print("\n" + response["output"] + "\n")
          
       except Exception as e:
           print(f"An error occurred: {e}")
