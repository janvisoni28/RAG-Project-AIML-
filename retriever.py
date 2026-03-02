import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vector.index")

# Load documents
with open("data/documents.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

def retrieve(query, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = [documents[i].strip() for i in indices[0]]
    return results