import json
from collections.abc import Callable
from config import WORKING_DIR

# list of available tools for the llm to use
available_tools: list = [

]

tool_map: dict[str, Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

# function that allows the agents to call selected tools
def call_tool(tool_call){

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
}
