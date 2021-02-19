"""Token helpers."""

from datetime import datetime, timedelta

import jwt

ALGORITHM = 'HS256'


def generate_token(
    data: dict,
    expires: timedelta,
    secret: str,
    algorithm: str = ALGORITHM,
) -> str:
    """Generates JWT token."""
    exp = datetime.utcnow() + expires
    payload = dict(data, exp=exp)
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
