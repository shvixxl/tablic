"""API dependencies."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.crud import users
from app.helpers.auth import verify_token
from app.schemas.auth import UserDB

oauth2 = OAuth2PasswordBearer(
    tokenUrl='/api/v1/auth/login'
)


async def get_user(
    token: str = Depends(oauth2),
) -> UserDB:
    """Validates token and returns user."""
    payload = verify_token(token, settings.SECRET_KEY)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials.",
        )

    user_id = payload.get('sub')
    user = await users.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return user
