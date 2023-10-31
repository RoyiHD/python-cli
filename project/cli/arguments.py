"""
CLI Module using arguments
"""
import click

@click.command()
@click.argument("file", type=click.STRING)
def main(file: str) -> None:
    """
    We can use the argument decorator for cli where a parameter is not optional
    """
    click.echo("Received file %s" % file)


if __name__ == "__main__":
    main()