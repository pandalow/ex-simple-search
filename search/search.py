from annoy import AnnoyIndex
import numpy as np
from .vectorize_query import vectorize_query


def get_index():
    features = np.load('data/s_bert_embeddings.npy').shape[1]
    u = AnnoyIndex(features, 'angular')
    u.load('data/course_index.ann')
    return u

def search_query(query):
    u = get_index()
    X = vectorize_query(query)
    nearest_ids = u.get_nns_by_vector(X, 10)
    return nearest_ids
