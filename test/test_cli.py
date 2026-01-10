from typer.testing import CliRunner

from pwd_gen.cli import app


def test_pwd(runner: CliRunner) -> None:
    result = runner.invoke(app, ["pwd"])
    output = result.stdout.strip()
    assert result.exit_code == 0
    assert len(output) == 64
    assert all(c in "0123456789abcdef" for c in output)


def test_pwd_urlsafe(runner: CliRunner) -> None:
    result = runner.invoke(app, ["pwd", "--urlsafe"])
    output = result.stdout.strip()
    assert result.exit_code == 0
    assert len(output) == 43
    assert not all(c in "0123456789abcdef" for c in output)


def test_rsa(runner: CliRunner) -> None:
    result = runner.invoke(app, ["rsa"])
    output = result.stdout.strip()
    assert result.exit_code == 0
    assert "-----BEGIN RSA PRIVATE KEY-----" in output
    assert "-----END RSA PRIVATE KEY-----" in output
    assert "-----BEGIN PUBLIC KEY-----" in output
    assert "-----END PUBLIC KEY-----" in output
