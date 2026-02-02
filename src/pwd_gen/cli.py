import typer

from pwd_gen import __version__, gen_pwd, gen_rsa

app = typer.Typer(
    no_args_is_help=True,
    help=f"pwd-gen {__version__} Yet another password generator.",
)


@app.command()
def pwd(
    nbytes: int = typer.Option(32),
    *,
    urlsafe: bool = typer.Option(default=False),
) -> None:
    if nbytes < 1:
        message = "nbytes must be >= 1"
        raise typer.BadParameter(message)
    typer.echo(gen_pwd(nbytes, urlsafe=urlsafe))


@app.command()
def rsa(
    public_exponent: int = typer.Option(65537),
    key_size: int = typer.Option(2048),
) -> None:
    if public_exponent not in [3, 65537]:
        message = "public_exponent must be 3 or 65537"
        raise typer.BadParameter(message)
    if key_size < 1024:  # noqa: PLR2004
        message = "key_size must be >= 1024"
        raise typer.BadParameter(message)
    key, pub = gen_rsa(public_exponent, key_size)
    typer.echo(key)
    typer.echo(pub)


def main() -> None:  # pragma: no cover
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
