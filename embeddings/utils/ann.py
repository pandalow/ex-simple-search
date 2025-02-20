from annoy import AnnoyIndex
import numpy as np

def build_index(output_path:str, index_path:str) -> str:

    s_bert_embeddings = np.load(output_path)

    samples, features = s_bert_embeddings.shape

    index = AnnoyIndex(features, 'angular')

    for i in range(samples):
        index.add_item(i, s_bert_embeddings[i])

    index.build(10)
    index.save(index_path)

    return "Success"