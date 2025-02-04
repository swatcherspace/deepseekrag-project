import ollama

def generate_embedding(text: str):
    response = ollama.embeddings(model="deepseek-r1:7b", prompt=text)
    return response["embedding"]  # Store as vector in DB
