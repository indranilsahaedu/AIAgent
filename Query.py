from google import genai
from google.genai import types
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore


#API Key Declearation
os.environ["PINECONE_API_KEY"] = "pcsk_3Kp5nv_5roLah5wvYz1gVs9wJrvruJBRKZ6YmzYkAtE6VPbY6KgKrGkVmi6igJjzee7Hvv"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDl-El5GBAkN9HyZ7o7-PpYCx36y138iLY"
client = genai.Client()
History=[]
def chat(userinput):
# try:
    
    History.append(
        {
            "role":"user",
            "parts":[{"text":userinput}]
        }
    )
    
    #1:-Questions convert into embedding 
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2", 
        output_dimensionality=768,
        task_type="retrieval_document"
    )

    queryvector=embeddings.embed_query(userinput)
    # print(queryvector)

    vector_store = PineconeVectorStore(index_name="indranil", embedding=embeddings)
    results = vector_store.similarity_search_by_vector(queryvector, k=3)
    # print(results)
    # for doc in results:
    #     print(doc.page_content)
    context_text = "\n\n".join([doc.page_content for doc in results])
    print(context_text)    

    response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=History,
                config=types.GenerateContentConfig(
                    system_instruction=f"""
            You are a chatbot. Your name is Neko. 
            First, state that you are an AI chatbot.
            Your task is to answer the user question based ONLY on the provided context.
            If the answer is not in the context, you must say: 'I don't have information about your question.'
            
            Context:
            {context_text}
            """
                    )
            )    
    History.append(
        {
            "role":"system",
            "parts":[{"text":response.text}]
        }
    ) 
    print(response.text)   
# except:
#     print("getting error")

def main():   
    while True:
        print(" ")
        userinput = input("Ask Me Anything (type 'exit' to quit): ")

        if userinput.lower() == "exit":
            print("Bye 👋")
            break
        chat(userinput)
main()