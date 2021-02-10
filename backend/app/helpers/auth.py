"""Helpers for authentication."""

import hashlib
import hmac
import bcrypt


def unicode_to_bytes(unicode: str) -> bytes:
    """Converts a unicode string to a bytes object."""
    if isinstance(unicode, str):
        return bytes(unicode, 'utf-8')
    return unicode


def generate_password_hash(password: str) -> bytes:
    """Generates a password hash using bcrypt."""
    if not password:
        raise ValueError('Password must be non-empty.')

    # Encode password as bytes before hashing.
    password = unicode_to_bytes(password)

    # Pre-hash password with SHA-256 to get rid of bcrypt limits (72 bytes)
    # and take its hexdigest to prevent NULL byte problems.
    password = hashlib.sha256(password).hexdigest()
    password = unicode_to_bytes(password)

    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password_hash(password: str, password_hash: str) -> bool:
    """Compares password and password hash."""

    # Encode strings as bytes before hashing.
    password = unicode_to_bytes(password)
    password_hash = unicode_to_bytes(password_hash)

    # Pre-hash password with SHA-256 to get rid of bcrypt limits (72 bytes)
    # and take its hexdigest to prevent NULL byte problems.
    password = hashlib.sha256(password).hexdigest()
    password = unicode_to_bytes(password)

    # Compare password and password hash in somewhat constant time.
    return hmac.compare_digest(
        bcrypt.hashpw(password, password_hash),
        password_hash
    )
