import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        workingdir_abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(workingdir_abs_path, file_path))
        valid_target_file = os.path.commonpath([workingdir_abs_path, target_path]) == workingdir_abs_path

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory' 
        
        os.makedirs(os.path.dirname(target_path), exist_ok=True) 

        with open(target_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
            return f'Error: {e}'
 
# schema_write_file = types.FunctionDeclaration(name="write_file",
#         description="Writes information we provide to the contents of a specified file relative to the working directory",
#         parameters=types.Schema(
#             type=types.Type.OBJECT,
#             required=["file_path", "content"],
#             properties={
#                 "file_path":types.Schema(
#                     type=types.Type.STRING,
#                     description="File path to the file that we want to write information to the contents of, relative to the working directory",
#                 ),
#                 "content":types.Schema(
#                     type=types.Type.STRING,
#                     description="Information that we want to write to the file given the file path",
#                 ),
#             }
#         )
#     )


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}