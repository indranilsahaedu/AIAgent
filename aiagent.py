from google import genai
from google.genai import types
client = genai.Client(api_key="AIzaSyA_C7FPCfmORlh1kNmOdVy5OPk8PRSPvuc")
def sum_numbers(num1, num2):
    return num1 + num2

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def annagram(str1, str2):
    return sorted(str1) == sorted(str2
)

sumdeclearation = {
    "name": "sum",
    "description": "get the sum of two number",
    "parameters": {
        "type": "object",
        "properties": {
            "num1": {
                "type": "number",
                "description": "first number"
            },
            "num2": {
                "type": "number",
                "description": "second number"
            }
        },
        "required": ["num1", "num2"]
    }
}

factorialdeclearation={
    "name":'factorial',
    "description":"get the Factorial of a number",
    "parameters":{
        "type":"object",
        "properties":{
            "num":{
                "type":"number",
                "description":"it will be the number for factorial example 10"
            },
        },
        "required":["num"]
    }

}

annagramdeclearation={
    "name":'annagram',
    "description":"check two string is annagram or not",
    "parameters":{
        "type":"object",
        "properties":{
            "str1":{
                "type":"string",
                "description":"it will be the first string for Annagram Check example Silent"
            },
            "str2":{
                "type":"STRING",
                "description":"it will be the second string for Annagram Check example lisent"
            },
        },
        "required":["str1","str2"]
    }
}

availabletool = {
    "sum": sum_numbers,
    "factorial": factorial,
    "annagram": annagram
}
def ai_agent(userinput):
    try:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=userinput)]
            )
        ]

        tools = types.Tool(
            function_declarations=[
                sumdeclearation,
                factorialdeclearation,
                annagramdeclearation
            ]
        )

        while True:

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction="You are a chatbot. Your name is Neko.first you told you are a ai chatbot" \
                    "you are a access of 3 available tools like sum of two numbers, check factorial, checka two string is annagram nor not" \
                    "use the tools whenever required to confirm userquery." 
                    "if user ask any general questions then don't reply and informwhat you can do very very politely",
                    tools=[tools]
                    )
            )

            if response.function_calls:

                call = response.function_calls[0]
                name = call.name
                args = call.args

                result = availabletool[name](**args)

                contents.append(response.candidates[0].content)

                contents.append(
                    types.Content(
                        role="user",
                        parts=[types.Part(
                            function_response={
                                "name": name,
                                "response": {"result": result}
                            }
                        )]
                    )
                )

            else:
                print("")
                print("NEKO: "+response.text)
                break    
    except:
        print("getting Errors")    
def main():
    while True:
        print(" ")
        userinput = input("Ask Me Anything (type 'exit' to quit): ")

        if userinput.lower() == "exit":
            print("Bye 👋")
            break

        ai_agent(userinput)
main()


