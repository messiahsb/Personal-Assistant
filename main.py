import os
import argparse
import json
import sys

from dotenv import load_dotenv
from openai import OpenAI
from prompts import sytem_prompt
from config import MAX_ITERS
from call_tools import available_tools, call_function

def main() -> None:
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
    # parser = argparse.ArgumentParser(description="Chatbot")
    # parser.add_argument("user_prompt", type=str, help="User prompt")
    # parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # args = parser.parse_args()

    # message history -> pass to agent for context and answer calling
    messages =[
        {"role": "system", "content": sytem_prompt},
            # {"role": "user", "content": args.user_prompt}
            ]
    # if args.verbose:
    #     print(f'User prompt: {args.user_prompt}\n')

    # while True:
#     user_input = input("\nYou: ")
#     if user_input.lower() == "exit":
#         break
#     messages.append({"role": "user", "content": user_input})
#     message = get_agent_chat(client, messages, True)
#     messages.append(message)
#     print("Response:")
#     print(message.content)

    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        return
    while True:
        try:
            # final_response = get_agent_chat(client, messages, args.verbose)
            messages.append({"role": "user", "content": user_input})
            final_response = get_agent_chat(client, messages, False)
            if final_response:
                print("Final response:")
                print(final_response)
                user_input = input("\nYou: ")
                if user_input.lower() == "exit":
                    return
        except Exception as e:
            print(f"Error in get_agent_chat: {e}")

    print(f"Maximum iterations ({MAX_ITERS}) reached")
    sys.exit(1)




# Function for agent chat
def get_agent_chat(client: OpenAI, messages: list, verbose: bool) -> str | None:
    response = client.chat.completions.create(
        model="gemma-4",
        messages=messages,
        tools=available_tools,
        # --- TOKEN OPTIMIZATIONS ---
            # max_tokens=200,               # Hard limit on output length
            temperature=0.5,             # Keep it focused and direct
            # stop=["User:", "Sure,"], # Stop the model from chatting extra
            stream=False
        )

    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    message = response.choices[0].message
    messages.append(message)

    if verbose:
        print(f'Prompt Tokens: {response.usage.prompt_tokens}')
        print(f'Response Tokens: {response.usage.completion_tokens}')

    if not message.tool_calls:
        return message.content

    for tool_call in message.tool_calls:
        if tool_call.type != "function":
            continue
        result_message = call_function(tool_call=tool_call)
        if not result_message.get('content'):
            raise RuntimeError(f"Empty function response for {tool_call.function.name}")
        if verbose:
            print(f"-> {result_message['content']}")
        messages.append(result_message)

    return None


if __name__ == "__main__":
    main()