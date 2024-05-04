from random import choice, randint
import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

def ask_openai(question):
    # Define the initial conversation context and capabilities of the assistant
    csv_file_path = 'MarchMadnessGames2023.csv'
    csv_file_path2 = 'MarchMadnessTeams2023.csv'
    with open(csv_file_path, 'r') as file:
      csv_text = file.read()
    with open(csv_file_path2, 'r') as file:
        csv_text2 = file.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable in Python programming, nutrition, and current events, especially in the sports world. Your name is Randolph. You are a university professor so speak your responses in a very knowledgeable manner. YOU ARE INFORMED by the march madness 2023 games which are given by: " + csv_text + ". You are also informed by the teams in march madness which are given by this csv" + csv_text2},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you are quiet'
    elif 'hello' in lowered:
        return 'Hello there! You need to code your AI Bot here'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}'
    elif 'help' in lowered:
        return f'you can say !data, !temp, or !pressure'
    else:
        return ask_openai(user_input)
    