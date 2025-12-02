import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        abs_directory_path = os.path.abspath(os.path.join(working_directory, directory)) if directory else os.path.abspath(working_directory)
        abs_working_directory = os.path.abspath(working_directory)
        
        if not abs_directory_path.startswith(abs_working_directory):
            return f"Error: {directory} is outside the {working_directory}" 
        if not os.path.isdir(abs_directory_path):  
            return f"Error: {directory} does not exist in {working_directory}"

        contents = os.listdir(abs_directory_path)
        result = ""

        for content in contents:
            content_path = os.path.join(abs_directory_path, content)
            is_dir = os.path.isdir(content_path)
            size = os.path.getsize(content_path)
            result += f" - {content}: file_size={size} bytes, is_dir={is_dir}\n"

        return result
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)