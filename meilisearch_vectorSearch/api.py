from fastapi import FastAPI
import uvicorn
from model import document_to_vector
import meilisearch

app = FastAPI()


@app.get("/search")
async def search(query: str):
    client = meilisearch.Client('http://localhost:7700')
    vector = document_to_vector(query).tolist()
    response = client.index('movies-vectorized').search("text",
                                                        {"hybrid": {"semanticRatio": 1.0, "embedder": "bart"},
                                                         "vector": vector})
    return {"documents": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
