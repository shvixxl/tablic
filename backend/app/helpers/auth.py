"""Helpers for authentication."""

import hashlib
import hmac
import bcrypt


def generate_password_hash(password: str) -> bytes:
    """Generates a password hash using bcrypt."""
    password = _clean_password(password)
    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password_hash(password: str, password_hash: str) -> bool:
    """Compares password and password hash."""

    password = _clean_password(password)
    password_hash = _unicode_to_bytes(password_hash)

    return hmac.compare_digest(
        bcrypt.hashpw(password, password_hash),
        password_hash
    )


def _unicode_to_bytes(unicode: str) -> bytes:
    """Converts a unicode string to a bytes object."""
    if isinstance(unicode, str):
        return bytes(unicode, 'utf-8')
    return unicode


def _prehash_password(password: bytes) -> bytes:
    """
    Pre-hash password with SHA-256 to get rid of bcrypt limits (72 bytes)
    and take its hexdigest to prevent NULL byte problems.
    """
    password = hashlib.sha256(password).hexdigest()
    password = _unicode_to_bytes(password)
    return password


def _clean_password(password: str) -> bytes:
    """
    Encodes password as bytes before hashing and pre-hashes it with SHA-256.
    """
    password = _unicode_to_bytes(password)
    password = _prehash_password(password)
    return password
