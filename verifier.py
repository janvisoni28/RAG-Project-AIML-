from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def faithfulness_score(answer, evidence):
    evidence_text = " ".join(evidence)

    emb1 = model.encode([answer])
    emb2 = model.encode([evidence_text])

    score = cosine_similarity(emb1, emb2)[0][0]
    return float(score)
    