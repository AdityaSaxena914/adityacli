import typer
from main import run_chat
from file_utils import read_file, get_project_files
from config import load_prompt, EXPLAIN_PROMPT_PATH, PROJECT_EXPLAIN_PROMPT_PATH,REVIEW_PROMPT_PATH, TEST_PROMPT_PATH, DIFF_PROMPT_PATH, CREATE_FILE_PROMPT_PATH
from chat import get_completion
from llm import get_client
from review import load_file_content
from diff_generator import generate_diff
from file_writer import write_file

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
    


@app.command()
def review(file_path: str):
    review_content = load_file_content(file_path)
    review_prompt = load_prompt(REVIEW_PROMPT_PATH)
    messages = [
        {
            "role": "system",
            "content": review_prompt
        },
        {
            "role": "user",
            "content": review_content
        }
    ]
    client = get_client()

    result = get_completion(
        client,
        messages
    )

    print(result)



@app.command()
def test(file_path: str):
    test_code = load_file_content(file_path)
    test_prompt = load_prompt(TEST_PROMPT_PATH)
    messages = [
        {
            "role": "system",
            "content": test_prompt
        },
        {
            "role": "user",
            "content": test_code
        }
    ]
    client = get_client()

    result = get_completion(
        client,
        messages
    )

    print(result)



@app.command()
def diff(file_path: str):
    original_conten = load_file_content(file_path)
    diff_prompt = load_prompt(DIFF_PROMPT_PATH)
    messages = [
        {
            "role": "system",
            "content": diff_prompt
        },
        {
            "role": "user",
            "content": original_conten
        }
    ]
    client = get_client()

    improved_content = get_completion(
        client,
        messages
    )
    print(
        generate_diff(
            original_conten, 
            improved_content
        )
    )


@app.command()
def create(file_path: str):
    user_request = input("What do you want to create? ")

    create_prompt = load_prompt(CREATE_FILE_PROMPT_PATH)

    messages = [
        {
            "role": "system",
            "content": create_prompt
        },
        {
            "role": "user",
            "content": user_request
        }
    ]

    client = get_client()

    result = get_completion(
        client,
        messages
    )

    write_file(
        file_path,
        result
    )

    print(f"Created {file_path}")


if __name__ == "__main__":
    app()