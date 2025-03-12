import threading
import heapq
import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Retriever:
    def __init__(self, embeddings, chunks):
        """Initializes the retriever with embeddings and text chunks."""
        if len(embeddings) != len(chunks):
            raise ValueError("Embeddings and chunks must have the same length.")

        self.embeddings = np.array(embeddings)  # Ensure numpy array for performance
        self.chunks = chunks
        self.results = []
        self.lock = threading.Lock()  # Ensures thread-safe operations

    def similarity_score(self, query_embedding, idx):
        """Computes similarity score and stores results safely."""
        try:
            score = cosine_similarity([query_embedding], [self.embeddings[idx]])[0][0]
            with self.lock:
                self.results.append((score, self.chunks[idx]))  # Thread-safe update
        except Exception as e:
            logging.error(f"Error computing similarity for index {idx}: {e}")

    def get_top_chunks(self, query_embedding, top_n=3):
        """Retrieves the top N most relevant chunks using multi-threading."""
        if len(self.embeddings) == 0:
            logging.warning("No embeddings available for retrieval.")
            return []

        threads = []
        for i in range(len(self.embeddings)):
            t = threading.Thread(target=self.similarity_score, args=(query_embedding, i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Efficiently get top-N results using heapq
        top_results = heapq.nlargest(top_n, self.results, key=lambda x: x[0])
        return top_results
