import ollama
import numpy as np
from sqlalchemy.future import select
from app.models import Document
from app.services.embedding import generate_embedding

async def get_relevant_docs(query: str, db):
    query_embedding = generate_embedding(query)

    # Fetch all documents
    result = await db.execute(select(Document))
    docs = result.scalars().all()

    # Compute cosine similarity
    similarities = []
    for doc in docs:
        doc_embedding = np.array(doc.embeddings)
        similarity = np.dot(query_embedding, doc_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding))
        similarities.append((doc, similarity))

    # Sort and return top 3 results
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [doc[0] for doc in similarities[:3]]

def generate_answer(query: str, docs):
    context = " ".join([doc.content for doc in docs])
    response = ollama.chat(model="deepseek-r1:7b", messages=[
        {"role": "system", "content": "Use the given documents to answer the question."},
        {"role": "user", "content": query + "\n\n" + context}
    ])
    return response["message"]["content"]
