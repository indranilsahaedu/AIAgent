from google import genai
from google.genai import types

History=[]

def chat(query):
    client = genai.Client(api_key="AIzaSyA_C7FPCfmORlh1kNmOdVy5OPk8PRSPvuc")

    # response = client.models.generate_content(
    #     model="gemini-3-flash-preview", 
    #     contents=query
    # )


    # response = client.models.generate_content(
    # model="gemini-3-flash-preview",
    # contents=query,
    # config=types.GenerateContentConfig(
    #     thinking_config=types.ThinkingConfig(thinking_level="low")
    # ),
    # )

    History.append(
        {
            "role":"user",
            "parts":[{"text":query}]
        }
    )
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a chatbot. Your name is Neko.first you told you are a ai chatbot"),
    contents=History
    )
    # print(History)
    # return response.text
    History.append(
        {
            "role":"system",
            "parts":[{"text":response.text}]
        }
    )
    print(response.text)
    # chat() 

def main():   
    while True:
        print(" ")
        userinput = input("Ask Me Anything (type 'exit' to quit): ")

        if userinput.lower() == "exit":
            print("Bye 👋")
            break
        chat(userinput)
main()