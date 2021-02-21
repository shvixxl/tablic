"""Token helpers."""

from datetime import datetime, timedelta

import jwt

ALGORITHM = 'HS256'


def generate_token(
    data: dict,
    secret: str,
    expires: timedelta = None,
    algorithm: str = ALGORITHM,
) -> str:
    """Generates JWT token."""
    payload = dict(data)
    if expires:
        exp = datetime.utcnow() + expires
        payload.setdefault('exp', exp)
    return jwt.encode(payload, secret, algorithm)


def verify_token(
    token: str,
    secret: str,
    algorithm: str = ALGORITHM,
) -> dict:
    """Verifies JWT token."""
    try:
        return jwt.decode(token, secret, algorithm)
    except jwt.PyJWTError:
        return None
