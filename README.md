# GenAI Movie Search (FAISS + LLM)

## Features
- Query movie data via /search?q=
- Embedding with SentenceTransformer
- Vector search with FAISS
- LLM response formatting (Gemini-ready)
- Update data daily with cron job

## Deployment
- Use GCP Cloud Run to deploy API
- Cloud Scheduler for daily `update_embeddings.py` job