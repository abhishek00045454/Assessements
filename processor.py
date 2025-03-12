import asyncio
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('stopwords')

class AsyncProcessor:
    """Asynchronous text processor for cleaning retrieved text chunks."""

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    async def clean_chunk(self, text):
        """Cleans a text chunk by tokenizing, removing non-alphabetic words, and filtering stopwords."""
        words = word_tokenize(text.lower())
        filtered_words = [w for w in words if w.isalpha() and w not in self.stop_words]
        return " ".join(filtered_words)

    async def process_chunks(self, chunks):
        """Processes multiple chunks asynchronously."""
        tasks = [self.clean_chunk(chunk) for chunk in chunks]
        return await asyncio.gather(*tasks)
