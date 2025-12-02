import os
from google.genai import types
MAX_CHARS = 10000
def get_files_content(file_path, working_directory):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_dir_path = os.path.abspath(working_directory)

    if not os.path.isfile(abs_file_path):
        return f"File: {file_path} does not exist"

    if not abs_file_path.startswith(abs_dir_path):
        return f"File: {file_path} is outside the {working_directory}"

    content = ""
    with open(abs_file_path, "r") as f:
        content += f.read()
        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS]
            content += f" [...File '{file_path}' truncated at 10000 characters]"
    return content

schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Get the contents of the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
            type=types.Type.STRING,
            description="Relative path of the file"
            )
        }
    )
)