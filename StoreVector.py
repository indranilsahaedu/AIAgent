
#Package declearition
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore


#API Key Declearation
os.environ["PINECONE_API_KEY"] = "pcsk_3Kp5nv_5roLah5wvYz1gVs9wJrvruJBRKZ6YmzYkAtE6VPbY6KgKrGkVmi6igJjzee7Hvv"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDl-El5GBAkN9HyZ7o7-PpYCx36y138iLY"

def storevector(filepath):
    try:
        #1:-Add PDF Document
        loader = PyPDFLoader(filepath)
        pages = loader.load()
        print("PDF Uploaded Sucessfully. Total Pages:- "+str(len(pages)))

        #2:- chunking Document
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000,    
            chunk_overlap=200,  
            length_function=len,
            is_separator_regex=False,
        )
        chunks = text_splitter.split_documents(pages)
        print(f"Created {len(chunks)} chunks from your PDF.")

        #3:-Declear Embedding Model
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-2", 
            output_dimensionality=768,
            task_type="retrieval_document"
        )

        #4:-Initializing Pinecone Client and stored chunks
        index_name = "indranil"
        vector_store = PineconeVectorStore.from_documents(
            documents=chunks,
            embedding=embeddings,
            index_name=index_name
        )
        print(vector_store)
        print("Vector Stored")
        return 0
    except:
        return 1
filepath="D:\\Indranil\\Indranil_Saha_Resume_V5.pdf"
storevector(filepath)

