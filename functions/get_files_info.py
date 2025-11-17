import os

def get_files_info(working_path, directory=None):
    try:
        abs_directory_path = os.path.abspath(os.path.join(working_path, directory))
        abs_working_path = os.path.abspath(working_path)
        
        if not abs_directory_path.startswith(abs_working_path):
            return f"Error: {directory} is outside the {working_path}" 
        if not os.path.isdir(abs_directory_path):  
            return f"Error: {directory} does not exist in {working_path}"

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