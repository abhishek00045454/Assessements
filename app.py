from flask import Flask, render_template, request, jsonify
import asyncio
from main import WikiExtractor, Embedder, Retriever, AsyncProcessor

app = Flask(__name__)

MODEL_PATH = "GoogleNews-vectors-negative300.bin"
embedder = Embedder(MODEL_PATH)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        query_text = data.get("query", "").strip()

        if not query_text:
            return jsonify({"error": "Query cannot be empty"}), 400

        url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        extractor = WikiExtractor(url)
        extractor.fetch_content()
        cleaned_text = extractor.clean_text()
        chunks = extractor.get_chunks()

        embeddings = embedder.parallel_embeddings(chunks)
        query_embedding = embedder.compute_embedding(query_text)

        retriever = Retriever(embeddings, chunks)
        top_chunks = retriever.get_top_chunks(query_embedding)

        processor = AsyncProcessor()
        processed_chunks = asyncio.run(processor.process_chunks([chunk for _, chunk in top_chunks]))

        response = [{"rank": i + 1, "text": chunk} for i, chunk in enumerate(processed_chunks)]
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
