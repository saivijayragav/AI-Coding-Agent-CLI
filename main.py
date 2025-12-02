from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys
from functions import schema_get_files_content, schema_get_files_info, schema_run_python_file, schema_write_file
from call_functions import call_functions

load_dotenv()

system_prompt = """
You are a helpful AI coding agent.
When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
- List files and directories
- Read files content
- Write content in files
- Excecute python files
All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
available_functions = types.Tool(
function_declarations=[schema_write_file, schema_get_files_content, schema_get_files_info, schema_run_python_file]
)


def main():
    client = genai.Client()
    args = sys.argv

    if len(args) <= 1:
        print("I need a prompt!")
        sys.exit(1)
    
    config = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    verbose_flag = False
    if len(args) == 3 and args[2] == "--verbose":
        verbose_flag = True
    prompt = args[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=config
        )
        
        if not response or not response.usage_metadata:
            print("Response is malformed")
            return 

        if verbose_flag:
            print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
            print("Response tokens: ", response.usage_metadata.candidates_token_count)

        if response.candidates:
            for candidate in response.candidates:
                if not candidate or not candidate.content:
                    continue
                messages.append(candidate.content)
        if response.function_calls:
            for function_call in response.function_calls:
                result = call_functions(function_call, verbose_flag)
                messages.append(result)
        else:
            print(response.text)
            return

    
if __name__ == "__main__":
    main()