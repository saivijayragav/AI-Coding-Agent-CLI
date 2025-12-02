import os
from google.genai import types
import re

DANGEROUS_PATTERNS = [
    r"os\.remove",
]

def is_dangerous(code):
    return any(re.search(p, code) for p in DANGEROUS_PATTERNS)

def write_file(working_directory, file_path, content):
    if is_dangerous(content):
        return "Dangerous code"
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_dir_path = os.path.abspath(working_directory)
    parent_dir = os.path.dirname(abs_file_path)

    if not abs_file_path.startswith(abs_dir_path):
        return f"Error: {file_path} is outside the {working_directory}"

    os.makedirs(parent_dir, exist_ok = True)    
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f"File: {file_path} written successfully. ({len(content)} characters written)"

    except Exception as e:
        return f"Error writing file: {file_path}. Exception: {str(e)}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write contents to a file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that needs to be written in the file."
            )
        },
    ),
)