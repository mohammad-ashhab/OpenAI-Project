import openai
from flask import current_app

def get_answer(question):
    openai.api_key = current_app.config['OPENAI_API_KEY']
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    
    answer = completion.choices[0].message['content']
    return answer
