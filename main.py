from typing import Union
from fastapi import FastAPI
from search import search_query
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Nothing here"}

@app.get("/search/{query}")
async def search(query: str):
    item_ids = search_query(query)  

   
    with open("data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    results = []
    for item_id in item_ids:
        for record in data:
            if record[0] == item_id:  
                results.append({"id": item_id, "title": record[1]})
                break

    return {"query": query, "results": results}
