import requests
from bs4 import BeautifulSoup
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WikiExtractor:
    def __init__(self, url):
        self.url = url
        self.text = ""

    def fetch_content(self):
        """Fetches Wikipedia content and extracts paragraphs."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            
            if not paragraphs:
                logging.warning("No paragraphs found on the page.")
                return
            
            self.text = " ".join(p.get_text(strip=True) for p in paragraphs)
            logging.info("Successfully fetched and extracted Wikipedia content.")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching content: {e}")
            raise

    def clean_text(self):
        """Cleans extracted text by removing extra spaces."""
        self.text = " ".join(self.text.split())  # Normalize spaces
        return self.text

    def get_chunks(self, chunk_size=100):
        """Splits the cleaned text into chunks of specified size."""
        words = self.text.split()
        chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
        
        if not chunks:
            logging.warning("No text found to split into chunks.")
        
        return chunks
