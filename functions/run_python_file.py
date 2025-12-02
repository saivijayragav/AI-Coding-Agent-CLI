import os
from google.genai import types
import subprocess 

def run_python_file(file_path, working_directory, args=[]):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_dir_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_dir_path):
        return f"Error: {file_path} is outside the {working_directory}"
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} does not exist"
    
    if not file_path.endswith(".py"):
        return f"Error: {file_path} is not a Python file"
    
    try:
        final_args = ["python", abs_file_path]
        if args:
            final_args.extend(args)
        result = subprocess.run(
            final_args,
            capture_output=True,
            timeout=30,
            cwd=working_directory
        )

        stdout = result.stdout.decode("utf-8")
        stderr = result.stderr.decode("utf-8")

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}. stderr: {stderr}"
        
        if not stdout:
            return "No output producesd."
        
        return f"""
        STDOUT: {stdout}
        STDERR: {stderr}
        Process exited with code {result.returncode}.
        """  
    except Exception as e:
        return f"Error running file: {file_path}. Exception: {str(e)}"       

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified python file, and return its results",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
            type=types.Type.STRING,
            description="Relative path of the file"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="An optional array of arguments that needs to be passed while executing the python program. It should be a list of strings."
            )
        }
    )
)