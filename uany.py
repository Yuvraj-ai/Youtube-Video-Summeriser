from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate   
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from pydantic import SecretStr

# from dotenv import load_dotenv

# load_dotenv()

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def create_vector_db_from_youtube_url(video_url : str, api_key: str) -> FAISS:
    loader  = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key= SecretStr(api_key))

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)
    
    db = FAISS.from_documents(docs,embeddings)
    
    return db

def get_response_from_query(db,query,api_key: str,k =4):
    #can handle only 4097 tokens
    
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join(d.page_content for d in docs)
    
    llm = llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=SecretStr(api_key),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
    )
    
    prompt  = PromptTemplate(
        input_variables = ["question", "docs"],
        template  = """You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed."""
    )
    
    chain  = LLMChain(llm = llm,prompt=prompt)
    
    response = chain.run(question = query, docs = docs_page_content)
    
    response = response.replace("\n", "  ")
    
    return response, docs
