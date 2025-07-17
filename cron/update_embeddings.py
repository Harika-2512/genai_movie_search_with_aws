import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.vod_client import fetch_movie_data

def update_index():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    movies = fetch_movie_data()
    df = pd.DataFrame(movies)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['title', 'description'], inplace=True)

    texts = (df['title'] + " " + df['description']).tolist()
    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    faiss.write_index(index, 'data/movies.index')
    df.to_csv('data/movies.csv', index=False)