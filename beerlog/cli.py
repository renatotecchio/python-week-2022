# import sys
# from .config import settings
import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console

# def main():
#    print("Hello from", settings.NAME)
#    print(sys.argv[1:])
#    for attr in sys.argv[1:]:
#        print("-> ", attr)

main = typer.Typer(help="Beer Management Application")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 beer added to database")
    else:
        print("🚨 Error to add register")


@main.command("list")
def list_beer(style: Optional[str] = None):
    """Lists beers in database"""
    beers = get_beers_from_database()
    table = Table(title="BeerLog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
        


