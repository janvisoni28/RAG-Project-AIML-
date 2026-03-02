from transformers import pipeline

# Lightweight model for Render free tier
generator = pipeline("text-generation", model="distilgpt2")

def generate_answer(query, evidence):
    context = " ".join(evidence)

    prompt = f"""
    Use ONLY the provided context to answer the question.
    If the answer is not present in context, say "Not found in evidence".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    output = generator(
        prompt,
        max_length=200,
        do_sample=False
    )

    answer = output[0]["generated_text"].split("Answer:")[-1].strip()
    return answer