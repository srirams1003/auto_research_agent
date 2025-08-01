# from agents.search_agent import search_agent
# from agents.pdf_agent import pdf_agent
# from agents.summarizer_agent import summarizer_agent
# from agents.synthesizer_agent import synthesizer_agent
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

   # Check if API key is set
   if not os.getenv("GEMINI_API_KEY"):
       print("❌ Error: GEMINI_API_KEY environment variable not set.")
       print("Please set your Gemini API key in a .env file or environment variable.")
       exit(1)

   # Get the agent executor
   try:
       agent_executor = get_research_agent()
       print("✅ Agent initialized successfully!")
   except Exception as e:
       print(f"❌ Error initializing agent: {e}")
       exit(1)

   # Example usage
   print("\n🤖 Research Agent is ready!")
   print("=" * 50)
   print("Available actions:")
   print("• Search for academic papers: 'Find papers about machine learning'")
   print("• Analyze specific papers: 'Analyze the paper at [PDF_URL]'")
   print("• Research topics: 'Research quantum computing applications'")
   print("• Type 'exit' or 'quit' to stop")
   print("=" * 50)

   while True:
       try:
           user_input = input("\n🔍 Enter your research query: ")
           if user_input.lower() in ["exit", "quit"]:
               print("👋 Goodbye!")
               break
           
           if not user_input.strip():
               print("Please enter a valid query.")
               continue
           
           print("\n🔄 Processing your request...")
           response = agent_executor.invoke({"input": user_input})
           print("\n📝 Response:")
           print(response["output"])
           
       except KeyboardInterrupt:
           print("\n👋 Goodbye!")
           break
       except Exception as e:
           print(f"❌ An error occurred: {e}")
           print("Please try again with a different query.")
