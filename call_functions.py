from google.genai import types
from functions import (
    get_files_content, get_files_info, run_python_file, write_file
)
functions = {
    "get_files_content": get_files_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}
working_directory = "./calculator"
def call_functions(functions_call_part, verbose=False):
    function_name, args = functions_call_part.name,functions_call_part.args
    if function_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    if verbose:
        print(f"--Calling function {function_name} with the arguments {args}")
    
    try:
        result = functions[function_name](working_directory=working_directory, **args)
    except Exception as e:
        result = f"Error: {e}"
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )