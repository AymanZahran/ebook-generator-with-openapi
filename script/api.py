import openai
import os

def call_openai(prompt, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response.choices[0].message['content'].strip()
