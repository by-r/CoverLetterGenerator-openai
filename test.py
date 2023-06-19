import openai

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY

""" response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
) """

prompt = input()

response = openai.Completion.create(
    model = 'text-curie-001',
    prompt = prompt,
    max_tokens = 512,
)
text = response['choices'][0]['text']

print(text)
print(response)