import typer
from main import run_chat
from file_utils import read_file, get_project_files
from config import load_prompt, EXPLAIN_PROMPT_PATH, PROJECT_EXPLAIN_PROMPT_PATH
from chat import get_completion
from llm import get_client



app = typer.Typer()

@app.command()
def chat():
    run_chat()

@app.command()
def explain(file_path: str):
    file_content = read_file(file_path)

    explain_prompt = load_prompt(
        EXPLAIN_PROMPT_PATH
    )

    messages = [
        {
            "role": "system",
            "content": explain_prompt
        },
        {
            "role": "user",
            "content": f"""
        File Name: {file_path}

        File Content:

        {file_content}
        """
        }
    ]
    
    client = get_client()

    result = get_completion(
        client,
        messages
    )

    print(result)

@app.command()
def project():
    files = get_project_files("src")

    project_prompt = load_prompt(PROJECT_EXPLAIN_PROMPT_PATH)
    project_content = ""

    for file_path in files:
        content = read_file(file_path)

        project_content += f"""

    FILE: {file_path}

    {content}

    """

    
    messages = [
        {
            "role": "system",
            "content": project_prompt
        },
        {
            "role": "user",
            "content": project_content
        }
    ]
    client = get_client()

    result = get_completion(
        client,
        messages
    )

    print(result)
    

if __name__ == "__main__":
    app()