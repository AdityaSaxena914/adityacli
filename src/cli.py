import typer
from main import run_chat

app = typer.Typer(invoke_without_command=True)

@app.callback()
def callback():
    run_chat()

if __name__ == "__main__":
    app()