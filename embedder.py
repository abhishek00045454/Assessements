import numpy as np
import multiprocessing
import logging
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Embedder:
    def __init__(self, model_path):
        """Loads the Word2Vec model."""
        try:
            self.model = KeyedVectors.load_word2vec_format(model_path, binary=True)
            self.vector_size = self.model.vector_size
            logging.info("Word2Vec model loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading Word2Vec model: {e}")
            raise

    def compute_embedding(self, text):
        """Computes embedding by averaging word vectors."""
        words = [w for w in word_tokenize(text.lower()) if w in self.model]

        if not words:
            logging.warning("No valid words found in text for embedding.")
            return np.zeros(self.vector_size)

        return np.mean([self.model[w] for w in words], axis=0)

    def parallel_embeddings(self, chunks):
        """Computes embeddings in parallel using multiprocessing."""
        num_workers = min(multiprocessing.cpu_count(), len(chunks))
        logging.info(f"Using {num_workers} processes for embedding computation.")

        with multiprocessing.Pool(processes=num_workers) as pool:
            embeddings = pool.map(self.compute_embedding, chunks)

        return np.array(embeddings)
