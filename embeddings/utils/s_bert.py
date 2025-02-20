from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import json


model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def embed_text(text):
    embeddings = model.encode(text)
    return np.array(embeddings,dtype=np.float32)


def process_data(file_path:str, output_path:str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame(data,columns=['id','title'])

    title = df['title'].tolist()

    embeddings = []
    for title in title:
        embeddings.append(embed_text(title))

    np.save(output_path,embeddings)

    return "Success"

