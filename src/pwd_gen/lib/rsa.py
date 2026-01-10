from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def gen_rsa(public_exponent: int, key_size: int) -> tuple[str, str]:
    key = rsa.generate_private_key(public_exponent, key_size)
    pub = key.public_key()
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        encryption_algorithm=serialization.NoEncryption(),
        format=serialization.PrivateFormat.TraditionalOpenSSL,
    ).decode(), pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()
