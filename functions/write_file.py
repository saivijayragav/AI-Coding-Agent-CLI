import os

def write_file(working_directory, file_path, content):
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