import numpy as np
import multiprocessing
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize

class Embedder:
    def __init__(self, model_path):
        self.model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    
    def compute_embedding(self, text):
        words = [w for w in word_tokenize(text.lower()) if w in self.model]
        if not words:
            return np.zeros(self.model.vector_size)
        return np.mean([self.model[w] for w in words], axis=0)

    def parallel_embeddings(self, chunks):
        with multiprocessing.Pool() as pool:
            embeddings = pool.map(self.compute_embedding, chunks)
        return embeddings
