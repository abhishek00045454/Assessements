import asyncio
import logging
from extractor import WikiExtractor
from embedder import Embedder
from retriever import Retriever
from processor import AsyncProcessor

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    """Main function to execute the pipeline."""
    try:
        url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        logging.info("Starting Wikipedia content extraction...")

        # Extract & clean text
        extractor = WikiExtractor(url)
        extractor.fetch_content()
        cleaned_text = extractor.clean_text()
        chunks = extractor.get_chunks()
        
        if not chunks:
            logging.error("No chunks were extracted from the text.")
            return
        
        logging.info(f"Extracted {len(chunks)} chunks from Wikipedia page.")

        # Generate embeddings using multiprocessing
        embedder = Embedder("GoogleNews-vectors-negative300.bin")  # Path to Word2Vec model
        embeddings = embedder.parallel_embeddings(chunks)
        
        if not embeddings:
            logging.error("Embedding generation failed.")
            return

        logging.info(f"Generated embeddings for {len(embeddings)} chunks.")

        # Query processing
        query = "What is the impact of AI?"
        logging.info(f"Processing query: {query}")

        query_embedding = embedder.compute_embedding(query)

        if query_embedding is None or not query_embedding.any():
            logging.error("Query embedding could not be generated.")
            return

        # Retrieve relevant chunks
        retriever = Retriever(embeddings, chunks)
        top_chunks = retriever.get_top_chunks(query_embedding)

        if not top_chunks:
            logging.warning("No relevant chunks retrieved.")
            return

        logging.info(f"Retrieved top {len(top_chunks)} relevant chunks.")

        # Async text processing
        processor = AsyncProcessor()
        processed_chunks = asyncio.run(processor.process_chunks([chunk for _, chunk in top_chunks]))

        # Output results
        logging.info("Final processed results:")
        for i, chunk in enumerate(processed_chunks):
            print(f"Rank {i+1}: {chunk}\n")

    except Exception as e:
        logging.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
