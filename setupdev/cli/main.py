import rich
import typer

app = typer.Typer(help="SetupDev - O orquestrador definitivo de ambientes de desenvolvimento.")

@app.command()
def status(word: str = typer.Argument("Dev", help="Uma palavra para testar o Rich")):
    """
    Exibe o status do ambiente atual (Comando de Teste).
    """
    rich.print(f"[italic red]Word: [/italic red][bold green]{word}[/bold green]")

if __name__ == "__main__":
    app()

