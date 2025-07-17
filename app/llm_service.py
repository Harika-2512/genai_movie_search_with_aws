import os
import openai
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  # Load .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_llm_response(results, query):
    # 1. Prepare context from search results
    context = "\n".join([
        f"Title: {r['title']}\nDescription: {r['description']}\nGenre: {r.get('genre', '')}\nActors: {r.get('actors', '')}"
        for r in results
    ])

    # 2. Create prompt
    prompt = (
        "You are a helpful movie recommendation assistant.\n"
        "Answer the user’s question based on the following movie data.\n"
        "Only use the information provided. If the answer isn't in the data, say 'I don't know'.\n\n"
        f"{context}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )

    client = OpenAI()

    # 3. Send prompt to OpenAI GPT
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers movie-related questions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    # 4. Return generated text
    return response.choices[0].message.content.strip()
