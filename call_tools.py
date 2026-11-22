import json
from collections.abc import Callable
from config import WORKING_DIR


from tools.get_file_content import schema_get_file_content, get_file_content
from tools.get_files_info import schema_get_files_info, get_files_info
from tools.run_python_file import schema_run_python_file, run_python_file
from tools.write_file import schema_write_file, write_file



# list of available tools for the llm to use
available_tools: list = [
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
]

tool_map: dict[str, Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

# # function that allows the agents to call selected tools
def call_function(tool_call) -> dict:

    tool_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or {})
    print(f' - Calling Tool: {tool_name}({function_args})')

    if tool_name not in tool_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown Tool: {tool_name}"
        }

    function_args["working_directory"] = WORKING_DIR
    result = tool_map[tool_name](**function_args)

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }

