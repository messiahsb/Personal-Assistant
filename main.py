import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# load api key and check to see if its valid
load_dotenv()
api_key = os.environ.get("LOCAL_API_KEY")

if not api_key:
    raise RuntimeError("local api environment variable not set")

# start the connect with the llm server
client = OpenAI(
    base_url = "http://192.168.144.1:1234/v1",
    api_key = api_key,
)

# Parser for Command Line chat with agent
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# message history -> pass to agent for context and answer calling
messages =[
    {"role": "system", "content": "You are a concise assistant. Answer in 1 paragraph or less. No preamble."},
        {"role": "user", "content": args.user_prompt}
        ]
if args.verbose:
    print(f'User prompt: {args.user_prompt}\n')

# Function for agent chat
def get_agent_chat(client: OpenAI, messages: list, verbose: bool) -> None:
    response = client.chat.completions.create(
        model="gemma-4",
        messages=messages,
        # --- TOKEN OPTIMIZATIONS ---
            # max_tokens=200,               # Hard limit on output length
            # temperature=0.5,             # Keep it focused and direct
            # stop=["User:", "Sure,"], # Stop the model from chatting extra
            stream=False
        )

    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    answer = response.choices[0].message.content
    if verbose:
        print(f'Prompt Tokens: {response.usage.prompt_tokens}')
        print(f'Response Tokens: {response.usage.completion_tokens}')
    print("Response:")
    print(answer)


get_agent_chat(client, messages, args.verbose)