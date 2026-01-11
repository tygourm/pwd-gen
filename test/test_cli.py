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


def test_pwd_invalid_nbytes(runner: CliRunner) -> None:
    result = runner.invoke(app, ["pwd", "--nbytes", "0"])
    output = result.stderr.strip()
    assert result.exit_code == 2
    assert "nbytes must be >= 1" in output


def test_rsa(runner: CliRunner) -> None:
    result = runner.invoke(app, ["rsa"])
    output = result.stdout.strip()
    assert result.exit_code == 0
    assert "-----BEGIN RSA PRIVATE KEY-----" in output
    assert "-----END RSA PRIVATE KEY-----" in output
    assert "-----BEGIN PUBLIC KEY-----" in output
    assert "-----END PUBLIC KEY-----" in output


def test_rsa_invalid_public_exponent(runner: CliRunner) -> None:
    result = runner.invoke(app, ["rsa", "--public-exponent", "7"])
    output = result.stderr.strip()
    assert result.exit_code == 2
    assert "public_exponent must be 3 or 65537" in output


def test_rsa_invalid_key_size(runner: CliRunner) -> None:
    result = runner.invoke(app, ["rsa", "--key-size", "512"])
    output = result.stderr.strip()
    assert result.exit_code == 2
    assert "key_size must be >= 1024" in output
