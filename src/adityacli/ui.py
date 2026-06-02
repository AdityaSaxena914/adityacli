from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.status import Status

console = Console()


def header_panel():
    header_panel = Panel(
        "[bold cyan]AdityaCLI[/bold cyan]\n"
        "Local-first AI Assistant",
        title="Welcome"
    )
    console.print(header_panel)
    console.print()


def render_dashboard(session_loaded: bool, message_count: int):

    model_panel = Panel(
        "[green]Model:[/green] Qwen3.5 9B\n"
        "[green]Backend:[/green] LM Studio",
        title="🤖 Model"
    )

    session_panel = Panel(
        f"[yellow]Loaded:[/yellow] {session_loaded}\n"
        f"[yellow]Messages:[/yellow] {message_count}",
        title="💾 Session"
    )

    console.print(
        Columns([model_panel, session_panel])
    )


def tool_status(tool: str, message: str):
    console.print(
        f"[bold blue][{tool}][/bold blue] {message}"
    )


def success(message: str):
    console.print(
        f"[bold green]✓[/bold green] {message}"
    )


def warning(message: str):
    console.print(
        f"[bold yellow]![/bold yellow] {message}"
    )


def error(message: str):
    console.print(
        f"[bold red]✗[/bold red] {message}"
    )


def thinking():
    return console.status(
        "[bold green]AdityaCLI is thinking..."
    )


def approval_panel(file_path: str):
    console.print(
        Panel(
            f"Target File:\n{file_path}",
            title="Edit Approval",
            border_style="yellow"
        )
    )