# NLP Query System using Flask & AI Processing 🚀

This is an AI-powered NLP Query System that extracts text from Wikipedia, processes it using embeddings, and retrieves relevant results based on user queries. The system is built using **Flask** for the backend and a simple **HTML/CSS/JavaScript** frontend.

## 📂 Project Structure
```
/nlp_project
│── /static
│   ├── styles.css       # Frontend CSS styles
│   ├── script.js        # Frontend JavaScript
│── /templates
│   ├── index.html       # Main HTML page
│── app.py               # Flask application
│── main.py              # NLP processing pipeline
│── extractor.py         # Wikipedia text extraction
│── embedder.py          # Text embedding generation
│── retriever.py         # Retrieving top chunks based on query
│── processor.py         # Async text processing
│── requirements.txt     # Required Python libraries
│── README.md            # Project documentation
```

---

## 1️⃣ Installation & Setup 🛠️

### Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/nlp-query-system.git
cd nlp-query-system
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

> Ensure you have **GoogleNews-vectors-negative300.bin** in the project directory for word embeddings.

---

## 2️⃣ Running the Flask App 🚀
```sh
python app.py
```
Then, open **http://127.0.0.1:5000/** in your browser.

---

## 3️⃣ Features 🏆
✔️ Fetches and cleans Wikipedia content  
✔️ Generates word embeddings using **Word2Vec**  
✔️ Uses **threading** for fast retrieval of relevant text  
✔️ Implements **async processing** for text cleaning  
✔️ Provides a web UI for querying AI-related topics  

---

## 4️⃣ API Endpoints 🔥
### Homepage
📌 **GET `/`**  
Returns the main webpage (index.html)

### Query API
📌 **POST `/query`**  
**Request:**  
```json
{
    "query": "What is the impact of AI?"
}
```
**Response:**  
```json
[
    {"rank": 1, "text": "AI is transforming industries like healthcare and finance..."},
    {"rank": 2, "text": "Machine learning models improve efficiency..."},
    {"rank": 3, "text": "Ethical concerns exist in AI decision-making..."}
]
```

---

## 5️⃣ Frontend UI 🌐
The frontend consists of:
- **index.html** → Form input for queries  
- **styles.css** → Clean, modern UI  
- **script.js** → Sends AJAX requests to the Flask backend  

Users can input their query, and the system will return **top 3 relevant Wikipedia excerpts**.

---

## 6️⃣ Contributing 🤝
If you’d like to contribute:
1. **Fork** this repo
2. **Create a branch:** `git checkout -b feature-branch`
3. **Commit changes:** `git commit -m "Added a new feature"`
4. **Push:** `git push origin feature-branch`
5. **Open a Pull Request`

---

## 7️⃣ Contact & Support 📩
📧 Email: abhisheksaini388@gmail.com  
🌍 GitHub: [github.com/yourusername](https://github.com/abhishek00045454)  

If you find this project useful, give it a ⭐️ on GitHub! 😊🎉
