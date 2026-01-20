# AlgoGenie - DSA Problem Solver

AlgoGenie is an intelligent AI-powered system that solves Data Structures and Algorithms (DSA) problems. It uses AutoGen agents to analyze problems, generate solutions, and execute code with Docker containerization.

## Features

✨ **AI-Powered Problem Solving**
- Uses OpenAI's GPT-4 model for intelligent problem analysis
- Generates optimized Python solutions with detailed explanations

🔧 **Automated Code Execution**
- Secure code execution in isolated Docker containers
- Comprehensive test case validation
- Real-time execution results and feedback

👥 **Multi-Agent Architecture**
- Problem Solver Agent: Analyzes DSA problems and creates solutions
- Code Executor Agent: Executes and validates code with test cases
- Collaborative round-robin team approach

🎨 **User-Friendly Interface**
- Streamlit web application for easy interaction
- Interactive task input and streaming responses
- Real-time progress updates

## Project Structure

```
AlgoGenie/
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── agents/
│   ├── problem_solver.py          # Problem solver agent implementation
│   └── code_executor_agent.py     # Code executor agent implementation
├── config/
│   ├── constant.py                # Project constants and settings
│   ├── docker_executor.py         # Docker execution logic
│   ├── docker_utils.py            # Docker utilities and helpers
│   └── settings.py                # Configuration and API setup
└── team/
    └── dsa_team.py                # Multi-agent team orchestration
```

## Prerequisites

- Python 3.8+
- Docker (for code execution in containers)
- OpenAI API Key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/D-e-v-e-s-h/DataScience.git
cd DataScience
```

### 2. Create Virtual Environment

```bash
python -m venv env-algogenie
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\env-algogenie\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source env-algogenie/bin/activate
```

### 4. Install Dependencies

```bash
cd AlgoGenie
pip install -r requirements.txt
```

## Configuration

### Setting Up Your OpenAI API Key

1. **Create a `.env` file in the AlgoGenie folder:**
   ```bash
   touch .env
   ```

2. **Add your OpenAI API key:**
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

3. **Verify the setup:**
   ```powershell
   python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
   ```

### Docker Setup

Make sure Docker is installed and running:

```bash
docker --version
docker run hello-world
```

## Usage

### Option 1: Web Interface (Streamlit)

```bash
cd AlgoGenie
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and enter your DSA problem statement.

### Option 2: Command Line

```bash
cd AlgoGenie
python main.py
```

This will execute a pre-defined problem (default: "write a python code to add two numbers").

### Example Input

```
Find the longest palindromic substring in a given string. 
The solution should handle edge cases and include multiple test cases.
```

## How It Works

1. **Problem Analysis**: The Problem Solver Agent analyzes your DSA problem
2. **Solution Generation**: Generates Python code with test cases
3. **Code Execution**: Executes the code in a secure Docker container
4. **Validation**: Validates results against test cases
5. **Output**: Returns explanation and solution code

## Dependencies

Key packages used in this project:

- `autogen-agentchat` - Multi-agent orchestration
- `autogen-core` - Core agent functionality
- `autogen-ext` - Extended features including OpenAI integration
- `streamlit` - Web application framework
- `python-dotenv` - Environment variable management
- `docker` - Docker container management

See `requirements.txt` for complete list.

## Security Notes

⚠️ **Important Security Practices:**

- Never commit `.env` file to GitHub (it's in `.gitignore`)
- Always use environment variables for sensitive data
- Keep your OpenAI API key confidential
- Code is executed in isolated Docker containers for safety

## Troubleshooting

### API Key Not Found
```
Error: No API key found
```
**Solution**: Ensure `.env` file is in the AlgoGenie folder with the correct API key.

### Docker Connection Error
```
Error: Cannot connect to Docker daemon
```
**Solution**: Ensure Docker is installed and running on your system.

### Module Not Found
```
ModuleNotFoundError: No module named 'autogen_agentchat'
```
**Solution**: Install dependencies: `pip install -r requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Author

**Devesh Phulara**

## Support

For questions and support, please open an issue on the GitHub repository.

---

**Note**: This project uses OpenAI's API which may incur costs. Please monitor your API usage.
