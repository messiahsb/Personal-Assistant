import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        workingdir_abs_path = os.path.abspath(working_directory)
        target_filepath = os.path.normpath(os.path.join(workingdir_abs_path, file_path))
        
        if os.path.commonpath([workingdir_abs_path, target_filepath]) != workingdir_abs_path:
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_filepath):
             return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_filepath, "r") as f:
            content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content

    except Exception as e:
            return f'Error: {e}'

# schema_get_file_content = types.FunctionDeclaration(name="get_file_content",
#         description="Returns the contents of a specified file relative to the working directory",
#         parameters=types.Schema(
#             type=types.Type.OBJECT,
#             required=["file_path"],
#             properties={
#                 "file_path":types.Schema(
#                     type=types.Type.STRING,
#                     description="File path to the file that we want to obtain the contents of, relative to the working directory",
#                 ),
#             }
#         )
#     )