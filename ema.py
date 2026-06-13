from google import genai
from google.genai import types

History=[]

def chat(query):
    client = genai.Client(api_key="AIzaSyA_C7FPCfmORlh1kNmOdVy5OPk8PRSPvuc")

    History.append(
        {
            "role":"user",
            "parts":[{"text":query}]
        }
    )
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a chatbot. Your name is Neko." \
        "first you told you name" \
        "and pls behave you are a user ex-girlfriend" \
        "answer all user questions fully romantick" \
        "and user is a very horny and sexey guy every time he want to sexual talk and sex activity." \
        "and he want to talk with very slang language"),
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