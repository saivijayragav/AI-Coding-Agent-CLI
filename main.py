from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys
from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
load_dotenv()


def main():
    client = genai.Client()
    args = sys.argv
    if len(args) <= 1:
        print("I need a fucking prompt!")
        sys.exit(1)

    verbose_flag = False
    if len(args) == 3 and args[2] == "--verbose":
        verbose_flag = True
    prompt = args[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    print(response.text)
    if verbose_flag:
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)
        return
    

# if __name__ == "__main__":
#     main()
print(get_files_content("calculator", "main.py"))
print(get_files_content("calculator", "pkg/calculator.py"))
print(get_files_content("calculator", "/bin/cat"))
print(get_files_content("calculator", "pkg/does_not_exist.py"))
print(get_files_content("calculator", "lorem.txt"))