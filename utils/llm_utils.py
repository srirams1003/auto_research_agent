import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role":"system", "content":"You are a helpful summarizer."},
                  {"role":"user", "content": text}]
    )
    return resp.choices[0].message.content.strip() 