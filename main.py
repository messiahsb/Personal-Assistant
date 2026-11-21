import os
from  dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("LOCAL_API_KEY")

if not api_key:
    raise RuntimeError("local api environment variable not set")

client = OpenAI(
    base_url = "http://192.168.144.1:1234/v1",
    api_key = api_key,
)

response = client.chat.completions.create(
    model="gemma-4",
    messages=[
        {
            "role": "user",
            "content": "can i run a local llm model directlty on my phone",
        }
    ],
)

answer = response.choices[0].message.content
print(answer)