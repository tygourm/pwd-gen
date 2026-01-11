from importlib.metadata import version

from .pwd import gen_pwd
from .rsa import gen_rsa

__version__ = version("pwd-gen")
__all__ = ["gen_pwd", "gen_rsa"]
