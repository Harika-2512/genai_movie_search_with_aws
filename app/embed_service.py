import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import os
import json
from app.utils import clean_text
from app.vod_client import fetch_movie_data

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_query_embedding(query):
    return model.encode([query])[0]

# Paths to your saved index and metadata
INDEX_PATH = "app/vectorstore/faiss_index.index"
META_PATH  = "app/vectorstore/movie_metadata.json"

def search_faiss_index(query_embedding, top_k: int = 5):
    """
    Retrieve the top‑k nearest movies for a given query embedding.

    Returns
    -------
    list[dict]
        Each dict contains the movie metadata plus a `distance` field
        (smaller distance ⇒ closer match).
    """
    # 1️⃣ Load FAISS index
    index = faiss.read_index(INDEX_PATH)

    # 2️⃣ Run ANN search
    D, I = index.search(np.asarray([query_embedding], dtype="float32"), top_k)

    # 3️⃣ Load metadata (list of dicts where list index == FAISS row id)
    with open(META_PATH, "r") as f:
        metadata = json.load(f)

    # 4️⃣ Assemble results
    results = []
    for distance, idx in zip(D[0], I[0]):
        if idx == -1:             # FAISS may return −1 for padding
            continue
        movie_entry = metadata[idx].copy()
        movie_entry["distance"] = float(distance)
        results.append(movie_entry)

    return results

def generate_embeddings(movie_data):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    descriptions = [clean_text(item['description']) for item in movie_data]
    embeddings = model.encode(descriptions, show_progress_bar=True)
    return embeddings

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def save_faiss_index(index, path="vectorstore/faiss_index.index"):
    faiss.write_index(index, path)

def save_metadata(movie_data, path="vectorstore/movie_metadata.json"):
    with open(path, "w") as f:
        json.dump(movie_data, f, indent=2)

def main():
    #with open("data/movies.json", "r") as f:
    #    movie_data = json.load(f)
    movie_data = fetch_movie_data()

    embeddings = generate_embeddings(movie_data)
    index = build_faiss_index(embeddings)

    os.makedirs("vectorstore", exist_ok=True)
    save_faiss_index(index)
    save_metadata(movie_data)

if __name__ == "__main__":
    main()
