from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()

def log_step(message: str):
    console.print(Panel.fit(f"[bold cyan]{message}[/bold cyan]", title="STEP", border_style="cyan"))

def log_info(message: str):
    console.print(f"[green]✓[/green] {message}")

def log_warn(message: str):
    console.print(f"[yellow]! {message}[/yellow]")

def log_error(message: str):
    console.print(f"[red]✗ {message}[/red]")

def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
