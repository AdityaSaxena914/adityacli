from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text

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

