# AI Coding Agent CLI

An intelligent command-line tool powered by Google's Gemini API that autonomously performs coding tasks through natural language requests.

## Overview

The AI Coding Agent is a sophisticated framework that enables you to interact with an AI assistant capable of understanding complex coding requirements and executing them independently. By leveraging Google's Gemini 2.5 Flash model, the agent can analyze your requests and intelligently chain multiple operations to accomplish your goals.

## Features

- 🤖 **AI-Powered Task Execution** - Use natural language to describe coding tasks
- 📁 **File Management** - Read, write, and inspect file structures
- 🐍 **Python Execution** - Run Python scripts and capture output
- 🔄 **Multi-turn Conversations** - Agent iteratively refines solutions through multiple function calls
- 📊 **Token Usage Tracking** - Monitor API usage with verbose mode
- 🎯 **Configurable Working Directory** - Scope operations to specific project folders

## Prerequisites

- Python 3.12 or higher
- Google Gemini API key (get one at [Google AI Studio](https://aistudio.google.com/app/apikeys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/saivijayragav/AI-Coding-Agent-CLI
cd AI-Coding-Agent-CLI
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

Add your Google API key to `.env`:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Quick Start

### Basic Usage

Ask the agent to perform a coding task:

```bash
python main.py "List all files in the calculator directory and show their content"
```

### With Verbose Output

See token usage and function calls:

```bash
python main.py "Write a new Python file that calculates fibonacci numbers" --verbose
```

## Available Operations

The AI agent has access to four core functions:

| Function | Purpose |
|----------|---------|
| `get_files_info` | List files and directories |
| `get_files_content` | Read file contents |
| `write_file` | Create or modify files |
| `run_python_file` | Execute Python scripts |

## How It Works

1. **Input Processing** - You provide a natural language prompt via CLI
2. **Agent Reasoning** - Gemini analyzes your request and creates a function call plan
3. **Function Execution** - The framework executes function calls in the designated working directory
4. **Iterative Refinement** - The agent reviews results and makes additional calls if needed (up to 20 iterations)
5. **Response** - Final result is presented back to you

## Project Structure

```
AI-Coding-Agent-CLI/
├── main.py                 # Entry point and agent orchestration
├── call_functions.py       # Function routing and execution
├── pyproject.toml          # Project metadata and dependencies
├── functions/              # Function implementations
│   ├── __init__.py
│   ├── get_files_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/             # Example project (default working directory)
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

## Configuration

The working directory can be configured in [call_functions.py](call_functions.py#L11):

```python
working_directory = "./calculator"
```

Modify this to target different project folders for the agent to work within.

## Example Use Cases

- **Code Generation** - Generate boilerplate or utility functions
- **File Organization** - Bulk rename, move, or organize files
- **Testing** - Create and run test suites
- **Documentation** - Generate or update documentation
- **Code Analysis** - Analyze codebase structure and content

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## Dependencies

- `google-genai>=1.50.1` - Google Gemini API client
- `python-dotenv>=1.2.1` - Environment variable management

## Limitations

- Maximum 20 iterations per request to prevent infinite loops
- Operations are scoped to the configured working directory
- Requires valid Google API credentials

## Error Handling

The agent includes built-in error handling for:
- Malformed API responses
- Unknown function calls
- Execution errors in called functions
- Invalid file paths

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Note**: Ensure you have sufficient API quota with Google Gemini for your use case, as each agent iteration consumes tokens.
