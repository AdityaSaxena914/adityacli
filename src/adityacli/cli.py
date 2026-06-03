import typer
from adityacli.chat_session import run_chat
from adityacli.file_utils import (
    read_file, 
    get_project_files,
    write_file
)

from adityacli.config import (
    load_prompt, 
    EXPLAIN_PROMPT_PATH, 
    PROJECT_EXPLAIN_PROMPT_PATH,
    REVIEW_PROMPT_PATH, 
    TEST_PROMPT_PATH, DIFF_PROMPT_PATH, 
    CREATE_FILE_PROMPT_PATH,
    EDIT_FILE_PROMPT_PATH
)

from adityacli.chat import get_completion
from adityacli.llm import get_client
from adityacli.diff_generator import generate_diff
from adityacli.ui import (
    console,
    tool_status,
    success,
    warning,
    error,
    thinking,
    approval_panel
)

from adityacli.tool_registry import (
    Tool,
    register_tool,
    list_tools
)



app = typer.Typer()

@app.command()
def chat():
    """Start an interactive chat session."""
    run_chat()


@app.command()
def explain(file_path: str):
    """Generate an explanation for the specified file.
    
    Args:
        file_path: The path to the file you want explained.
    """

    tool_status(
        "FILE",
        f"Reading {file_path}"
    )

    file_content = read_file(file_path)

    tool_status(
        "LLM",
        "Generating explanation"
    )

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

    with thinking():
        result = get_completion(
            client,
            messages
        )

    print(result)



@app.command()
def project(folder_path: str):
    """Analyze and explain the entire project folder.
    
    Args:
        folder_path: The path to the project directory you want analyzed.
    """

    tool_status(
        "FILE",
        "Scanning project files"
    )

    files = get_project_files(folder_path)

    tool_status(
        "FILE",
        f"Found {len(files)} files"
    )

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

    with thinking():
        result = get_completion(
            client,
            messages
        )

    print(result)
    


@app.command()
def review(file_path: str):
    """Review the code quality of a specific file.
    
    Args:
        file_path: The path to the file you want reviewed.
    """
    
    tool_status(
        "Review", 
        f"{file_path}"
    )


    review_content = read_file(file_path)
    review_prompt = load_prompt(REVIEW_PROMPT_PATH)

    
    tool_status(
        "LLM", 
        "Reviewing..."
    )

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

    with thinking():
        result = get_completion(
            client,
            messages
        )
    print(result)



@app.command()
def test(file_path: str):
    """Generate pytest tests for a specific file.
    
    Args:
        file_path: The path to the source code file you want tested against.
    """
    
    tool_status(
        "Test Generation", 
        f"{file_path}"
    )
    test_code = read_file(file_path)
    test_prompt = load_prompt(TEST_PROMPT_PATH)

    
    tool_status(
        "LLM", 
        "Generating Test using pytest...."
    )

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

    with thinking():
        result = get_completion(
            client,
            messages
        )

    print(result)



@app.command()
def diff(file_path: str):
    """Suggest improvements and show the diff for a specific file.
    
    Args:
        file_path: The path to the file you want improved.
    """
    tool_status(
        "FILE",
        f"Reading {file_path}"
    )

    original_content = read_file(file_path)

    diff_prompt = load_prompt(
        DIFF_PROMPT_PATH
    )

    messages = [
        {
            "role": "system",
            "content": diff_prompt
        },
        {
            "role": "user",
            "content": original_content
        }
    ]

    client = get_client()

    tool_status(
        "LLM",
        "Generating improved version"
    )

    with thinking():
        improved_content = get_completion(
            client,
            messages
        )

    tool_status(
        "DIFF",
        "Comparing versions"
    )

    print(
        generate_diff(
            original_content,
            improved_content
        )
    )


@app.command()
def create(file_path: str):
    """Create a new file based on user input.
    
    Args:
        file_path: The path where the new file should be created.
    """
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

    tool_status(
        "CREATE",
        f"Creating {file_path}"
    )

    tool_status(
        "LLM",
        "Generating file content"
    )

    with thinking():
        result = get_completion(
            client,
            messages
        )

    tool_status(
        "WRITE",
        f"Writing {file_path}"
    )

    write_file(
        file_path,
        result
    )

    success(
        f"Created {file_path}"
    )




@app.command()
def edit(file_path: str):
    """Edit an existing file based on user input.
    
    Args:
        file_path: The path to the file you want to modify.
    """

    tool_status(
        "FILE",
        f"Reading {file_path}"
    )


    original_content = read_file(file_path)

    tool_status(
        "LLM",
        "Generating modifications"
    )

    edit_request = input(
        "What changes should be made? "
    )

    edit_prompt = load_prompt(
        EDIT_FILE_PROMPT_PATH
    )

    messages = [    
        {
            "role": "system",
            "content": edit_prompt
        },
        {
            "role": "user",
            "content":
            f"""
    Request:
    {edit_request}

    File:
    {original_content}
    """
        }
    ]

    client = get_client()

    with thinking():
        updated_content = get_completion(
            client,
            messages
        )
    
    tool_status(
        "DIFF",
        "Comparing changes"
    )
    
    diff = generate_diff(
            original_content,
        updated_content
    )

    print(diff)
    
    approval_panel(file_path)
    
    while True:
        choice = input(
            "\nApply changes? (y/n): "
        ).strip().lower()
        if choice == "y":
            write_file(
                file_path,
                updated_content
            )

            success("Changes applied.")
            break
        elif choice == "n":
            warning("Changes discarded.")
            break
        else:
            error("Invalid choice! Enter y or n...")
            


@app.command()
def tools():
    categories = {}

    for tool in list_tools():
        if tool.category not in categories:
            categories[tool.category] = []

        categories[tool.category].append(tool)

    for category, tools in categories.items():
        console.print(f"\n[{category}]")

        for tool in tools:
            console.print(
                f"  {tool.name} - {tool.description}"
            )




register_tool(
    Tool(
        name="review",
        description="Review source code",
        category="CODE",
        handler=review
    )
)

register_tool(
    Tool(
        name="test",
        description="Generate tests",
        category="CODE",
        handler=test
    )
)

register_tool(
    Tool(
        name="diff",
        description="Generate diffs",
        category="CODE",
        handler=diff
    )
)

register_tool(
    Tool(
        name="create",
        description="Create files",
        category="FILE",
        handler=create
    )
)

register_tool(
    Tool(
        name="edit",
        description="Edit files",
        category="FILE",
        handler=edit
    )
)

register_tool(
    Tool(
        name="chat",
        description="Interactive chat session",
        category="CORE",
        handler=chat
    )
)

register_tool(
    Tool(
        name="explain",
        description="Explain a source file",
        category="ANALYSIS",
        handler=explain
    )
)

register_tool(
    Tool(
        name="project",
        description="Analyze an entire project",
        category="ANALYSIS",
        handler=project
    )
)


if __name__ == "__main__":
    app()