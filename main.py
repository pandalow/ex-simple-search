from typing import Union
from fastapi import FastAPI
from search import search_query
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Nothing here"}

@app.get("/search/{query}")
async def search(query: str):
    item_ids = search_query(query)
    return {"item_ids": item_ids}