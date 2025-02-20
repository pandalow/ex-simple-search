## EX-SIMPLE SEARCH ENGINE

### Overview

This is an extremely simple search engine built with Spotify Annoy and SBERT Embeddings. It is designed for fast similarity search and is implemented using FastAPI.

### Embedding Model

- SBERT Model: all-mpnet-base-v2 from Sentence Transformers
- Embedding Dimension: 768
- Indexing Library: Annoy (Approximate Nearest Neighbors)

### Features

- Provides one API endpoint to retrieve the top 10 most similar IDs for a given text query.
- Supports fast approximate nearest neighbor search.
- Lightweight, no database interactions or security layers (can be added if needed).

### Installation and Setup

#### Install Dependencies
You can install the required dependencies using Conda or pip:

- Option 1: Using Conda
`conda install --file requirements.txt`
- Option 2: Using pip
`pip install -r requirements.txt`
#### Prepare Your Data
The search engine requires an indexing JSON file stored in /data/data.json. The file should be formatted as follows:
Example Data Format (data/data.json)
```
[
    [1, "Key Issues / Education and the Arts"],
    [2, "Public Funding - Practitioners' Approaches"],
    [3, "Creative Process/Theatre in Ireland"]
]
```
#### Generate Embeddings and Index
Before starting the search engine, you need to generate SBERT embeddings and build an Annoy index.
Run the embedding script:`python embeddings/script.py`
This will generate:
- `sbert_embeddings.npy` → Stores the SBERT-generated embeddings.
- `index.ann` → Stores the Annoy index for fast retrieval.
#### Start the FastAPI Server
Run the following command to start the search engine server:
- `fastapi dev main.py`
The default API will be available at:
Swagger UI Docs: http://127.0.0.1:8000/docs
ReDoc API Docs: http://127.0.0.1:8000/redoc

### API Documentation
Endpoint: Search Similar Texts
Method: GET
URL: `/search/{query}`
Description: Returns the top 10 most similar results based on the input query.
Example Request:
`curl -X GET "http://127.0.0.1:8000/search/computer" -H "accept: application/json"`
Example Response:
```
{
    "query": "science",
    "results": [
        {"id": 2101, "title": "Teaching for Active Learning"},
        {"id": 7928, "title": "Literature Review"},
        {"id": 7930, "title": "Biometry - Statistics for Biologists"},
        {"id": 522, "title": "Biomedical Engineering and Medicine"},
    ]
}
```
### Security and Deployment Notes

- No authentication or authorization is implemented (Add JWT, OAuth if needed).
- No database interaction (This is a standalone lightweight service).
- For production, use gunicorn or uvicorn with multiple workers:
`uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4`
- Can be deployed using Docker (Dockerfile not included in this repo).

### References
Sentence Transformers: https://sbert.net/docs/quickstart.html
Spotify Annoy: https://github.com/spotify/annoy
FastAPI: https://fastapi.tiangolo.com

Happy Searching! 🎯
