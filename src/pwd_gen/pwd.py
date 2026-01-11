import secrets


def gen_pwd(nbytes: int, *, urlsafe: bool) -> str:
    return secrets.token_urlsafe(nbytes) if urlsafe else secrets.token_hex(nbytes)
