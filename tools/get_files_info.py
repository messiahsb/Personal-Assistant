import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        output = ""
        for filename in os.listdir(target_dir):
                filepath = os.path.join(target_dir, filename)
                # checks if the current item is a directory returns a bool
                is_dir = os.path.isdir(filepath)
                # gets the file size in bytes to return in the output
                file_size = os.path.getsize(filepath)

                output += f"- {filename}: file_size: {file_size} bytes, is_dir={is_dir}\n"
        return output

    except Exception as e:
        return f"Error: listing files{e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}