import rich
import typer
from pathlib import Path
from setupdev.core.orchestrator import orchestrate
from setupdev.adapters.tmux import TmuxAdapter

app = typer.Typer(help="SetupDev - O orquestrador definitivo de ambientes de desenvolvimento.")

@app.command()
def start():
    root_path = Path.cwd()
    rich.print(f"[bold yellow]Starting SetupDev on: [/bold yellow][bold cyan]{root_path}[/bold cyan]")

    tmux_driver = TmuxAdapter(root_path.name)
    orchestrate(root_path, tmux_driver)

if __name__ == "__main__":
    app()
