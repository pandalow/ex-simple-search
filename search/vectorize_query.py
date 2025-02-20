from sentence_transformers import SentenceTransformer

def get_vectorizer():
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    return model

def vectorize_query(query):
    vectorizer = get_vectorizer()
    X = vectorizer.encode(query)
    return X

