import requests
import ollama
from ollama import chat
from ollama import ChatResponse

text_file = 'text_file.txt'
user_input = input("Enter your horoscope sign: ")
model='llama3'

with open('text_file.txt', 'r') as f:
    text = f.read().strip()

prompt = f"""You're a fortune teller who tells horoscopes of different signs.
Please see the {user_input} for the sign that the user has inputted. Then look for that
signs horoscope in {text} and tell that horoscope to the user in a mom way. That is
be sarcastic, kind and you have to tell the horoscopes in grade 5 level english. Use
short sentences, be pessimistic, rude, judgemental too. Dont write everything
related to horoscope sign. Make fun of the user. 
Don't write the sign name while telling the horoscope. Don't write more than 5-10 lines.
"""

response = ollama.generate(model=model, prompt=prompt)
generated_horoscope = response.get('response', '')
print(generated_horoscope)