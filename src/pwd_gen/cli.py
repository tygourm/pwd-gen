from importlib.metadata import version

import typer

from .lib import gen_pwd, gen_rsa

app = typer.Typer(
    no_args_is_help=True,
    help=f"pwd-gen {version('pwd-gen')} Yet another password generator.",
)


@app.command()
def pwd(
    nbytes: int = typer.Option(32),
    *,
    urlsafe: bool = typer.Option(default=False),
) -> None:
    typer.echo(gen_pwd(nbytes, urlsafe=urlsafe))


@app.command()
def rsa(
    public_exponent: int = typer.Option(65537),
    key_size: int = typer.Option(2048),
) -> None:
    key, pub = gen_rsa(public_exponent, key_size)
    typer.echo(key)
    typer.echo(pub)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
