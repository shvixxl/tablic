"""Token helpers."""

from typing import Any, Optional
from datetime import datetime, timedelta

import jwt

ALGORITHM = 'HS256'


async def generate_token(
    subject: Any,
    expires: timedelta,
    secret: str,
    algorithm: str = ALGORITHM,
) -> str:
    """Generates JWT token."""
    exp = datetime.utcnow() + expires
    payload = {'exp': exp, 'sub': str(subject)}
    return jwt.encode(payload, secret, algorithm)


async def verify_token(
    token: str,
    secret: str,
    algorithm: str = ALGORITHM,
) -> Optional[str]:
    """Verifies JWT token."""
    try:
        return jwt.decode(token, secret, algorithm).get('sub')
    except jwt.PyJWTError:
        return None
