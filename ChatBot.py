"""
Author: - CodeBuzz (Advait Muley)
Project Name: - AI Chatbot
API use: - OpenAI
"""
import openai
import sys

key = "YOUR_API_KEY"

def quit():
    sys.exit()
    
while 0>-1:
    openai.api_key = key

    model_engine = "text-davinci-003"
    prompt = str(input(""))
    
    if prompt == "chat.exit":
        quit()        
    
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1, 
        )
    
    response = completion.choices[0].text
    print(response)
