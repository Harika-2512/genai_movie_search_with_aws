from fastapi import FastAPI, Query
from app.embed_service import get_query_embedding, search_faiss_index
from app.llm_service import get_llm_response

app = FastAPI()

@app.get("/search")
def search_movies(q: str = Query(...)):
    query_embedding = get_query_embedding(q)
    results = search_faiss_index(query_embedding)
    answer = get_llm_response(results, q)
    return {"answer": answer}