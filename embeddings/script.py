from utils.s_bert import process_data
from utils.ann import build_index

args = {
    'file_path': 'data/data.json',
    'output_path': 'data/s_bert_embeddings.npy',
    'index_path': 'data/index.ann'
}


if __name__ == '__main__':
    process_data(args['file_path'], args['output_path'])
    build_index(args['output_path'], args['index_path'])

