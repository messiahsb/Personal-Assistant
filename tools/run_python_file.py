import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        working_absolute = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_absolute, file_path))

        # checks to see if file path is outside of the working directory
        if os.path.commonpath([working_absolute, target_path]) != working_absolute:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # checks to see if file path points to file and exists
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        if file_path[-3:] != '.py':
            return f'Error: "{file_path}" is not a Python file'
    
        command = ["python", target_path]

        if args is not None:
            command.extend(args)

        completed_process = subprocess.run(command, cwd=working_absolute, text=True, capture_output=True, timeout=30)

        output =""
        if completed_process.returncode != 0:
             output = " ".join([output,f"Process exited with code {completed_process.returncode}"])
        if not completed_process.stderr  and not completed_process.stdout:
            output = " ".join([output,"No output produced"])
        if completed_process.stdout: 
            output =" ".join([output, f'STDOUT: {completed_process.stdout}'])
        if completed_process.stderr: 
            output =" ".join([f'\nSTDERR: {completed_process.stderr}'])
        return output

    except Exception as e:
        return f'Error: {e}'


# schema_run_python_file = types.FunctionDeclaration(name="run_python_file",
#         description="Runs a python file in a specified direcory relative to the working directory, proving the output of the run file",
#         parameters=types.Schema(
#             type=types.Type.OBJECT,
#             required=["file_path"],
#             properties={
#                 "file_path":types.Schema(
#                     type=types.Type.STRING,
#                     description="File path to the function that we want to run, relative to the working directory ",
#                 ),
#                 "args":types.Schema(
#                     type=types.Type.ARRAY,
#                     items=types.Schema(type=types.Type.STRING),
#                     description="arguments to the specified function of the file that we want to run (default is None)", 
#                 )
#             }
#         )
#     )