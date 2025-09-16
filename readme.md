# 🎥 YouTube Video Summeriser Assistant using Google Gemini AI + LangChain + Streamlit

This project is an intelligent YouTube assistant that allows you to query any YouTube video and get meaningful, context-rich answers based solely on the video’s transcript. It uses **LangChain**, **Google Gemini AI**, **FAISS**, and **Streamlit** to create a vector-based retrieval-augmented generation (RAG) system.

---

## 🚀 Features

- Extracts transcripts from YouTube videos using `YoutubeLoader`
- Embeds transcripts using `GoogleGenerativeAIEmbeddings`
- Stores embeddings in a FAISS vector store
- Uses Gemini (Google Generative AI) LLM to answer queries
- Fully interactive via a web UI (Streamlit)
- Securely accepts Gemini API Key at runtime (no `.env` required)

---

##  Demo

![Screenshot](/Screenshot.png) 

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/youtube-assistant.git
cd youtube-assistant
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Fedora/Linux
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Usage

### 1. Run the Streamlit app
```bash
streamlit run main.py
```
### 2. In the sidebar:
- Paste your Gemini API key ([from Google AI Console](https://aistudio.google.com/app/apikey))

- Enter a valid YouTube video URL

- Ask your question related to the video content

- Get detailed answers!

---

##  Project Structure

```bash
├── main.py             # Streamlit frontend
├── uany.py             # Core LangChain logic (embedding, retrieval, generation)
├── requirements.txt    # Required Python packages
├── README.md           # This file
```

---

##  Requirements

Here’s a sample of what’s inside requirements.txt:

```bash
streamlit
langchain
langchain-community
langchain-google-genai
langchain-core
google-api-python-client
python-dotenv
```

Though it is adviced to use [requirements.txt]() file only.

---

##  Security

- This app does not save your API key anywhere.

- It takes your Gemini API key at runtime and uses it only in memory.

---

##  License

This project is licensed under the  GPL-3.0 license.

---

##  Acknowledgements

- [LangChain](https://www.langchain.com/)

- [Google Gemini API](https://ai.google.dev/)

- [Streamlit](https://streamlit.io/)

- [FAISS](https://github.com/facebookresearch/faiss)

---

##  Future Improvements

-    Add support for multilingual transcripts

-    Add LLM response sources/trace visualization

-    Export answers as PDF or Markdown

-    UI enhancements

---

