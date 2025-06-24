import requests
import ollama
from ollama import chat
from ollama import ChatResponse

def get_horoscope(sign: str, day: str = 'TODAY'):
    base_url = 'https://horoscope-app-api.vercel.app/get-horoscope/daily?'
    params = {
        'sign': sign.capitalize(),
        'day': day.upper()
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        return data.get('horoscope_data', 'No horoscope found')
    except Exception as e:
        return f"Error fetching horoscope: {e}"
    
user_input = input("Enter your horoscope sign: ").strip()

horoscope_text = get_horoscope(user_input)

message = [
    {
        'role': 'user',
        'content': f"""You're a fortune teller who tells horoscopes of different signs.
The horoscope of the user is {horoscope_text} tell that horoscope to the user in a mom way. That is
be sarcastic, kind and you have to tell the horoscopes in grade 5 level english. Use
short sentences, be pessimistic, rude, judgemental too. Dont write everything
related to horoscope sign. Make fun of the user. 
Don't write the sign name while telling the horoscope. Don't write more than 5-10 lines.
"""
    }
]

stream = chat(
    model='llama3',
    messages=message,
    stream=True,
)
for chunk in stream:
    print(chunk['message']['content'],end='',flush=True)
# response = ollama.generate(model=model, prompt=prompt)
# generated_horoscope = response.get('response', '')
# print(generated_horoscope)