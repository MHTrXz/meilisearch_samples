from fastapi import FastAPI
import uvicorn
from model import document_to_vector
import meilisearch
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/search")
async def search(query: str):
    client = meilisearch.Client('http://localhost:7700')
    vector = document_to_vector(query).tolist()
    response = client.index('movies-vectorized').search(query,
                                                        {"hybrid": {"semanticRatio": 1.0, "embedder": "bart"},
                                                         "vector": vector})
    return response


@app.get("/keyword-search")
async def keyword_search(query: str):
    client = meilisearch.Client('http://localhost:7700')
    response = client.index('movies-vectorized').search(query)
    return response


@app.get("/hug-search")
async def hug_search(query: str):
    client = meilisearch.Client('http://localhost:7700')
    response = client.index('movies-vectorized').search(query,
                                                        {"hybrid": {"semanticRatio": 1.0, "embedder": "huggingFace"}})
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
