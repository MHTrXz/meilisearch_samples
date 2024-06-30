import json
from fastapi import FastAPI, Path
from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


# Function to convert a document to a BERT vector
def document_to_vector(doc):
    inputs = tokenizer(doc, return_tensors='pt', truncation=True, padding='max_length', max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


# Example documents
documents = [
    "This is a sample document.",
    "Another document for testing.",
    "Neural networks are powerful for natural language processing."
]

# example query: How do neural networks work?

# Convert documents to vectors
vectors = np.array([document_to_vector(doc) for doc in documents])


# Function to perform a cosine similarity search
def search_documents(query, documents, vectors):
    query_vector = document_to_vector(query).reshape(1, -1)
    similarities = cosine_similarity(query_vector, vectors).flatten()
    sorted_indices = similarities.argsort()[::-1]

    results = [(documents[idx], similarities[idx]) for idx in sorted_indices]
    return results


@app.get('/vectoriz')  # query parameter route
def get_by_name(vectorized: str):
    return json.dumps({'data': document_to_vector(vectorized).reshape(1, -1).astype('str').tolist()[0]})


@app.get('/search')  # query parameter route
def get_by_name(query: str):
    out = []
    for i, (doc, similarity) in enumerate(search_documents(query, documents, vectors)):
        out.append(f"Document: {doc} - Similarity: {similarity:.4f}")
    return json.dumps({'data': out})
