"""Auth services with bussines logic."""

from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm

from ..config import ACCESS_TOKEN_EXPIRE_DAYS, SECRET_KEY
from ..crud.auth import CRUDUser
from ..exceptions import UserAlreadyExists
from ..schemas.auth import UserIn, UserDB
from ..helpers.auth import (
    generate_password_hash,
    check_password_hash,
    generate_token,
)


async def create_user(
    user: UserIn,
    users: CRUDUser
) -> UserDB:
    """Service for creating new User."""
    existing_user = await users.get_by_email(user.email)

    if existing_user:
        raise UserAlreadyExists()

    password_hash = generate_password_hash(user.password)
    user_db = UserDB(**user.dict(), password_hash=password_hash)

    return await users.create(user_db)


async def authenticate_user(
    credentials: OAuth2PasswordRequestForm,
    users: CRUDUser
) -> Optional[UserDB]:
    """Service for authenticating User."""
    user = await users.get_by_email(credentials.username)

    if not user:
        # Run the hasher to mitigate timing attack
        generate_password_hash(credentials.password)
        return None

    if not check_password_hash(credentials.password, user.password_hash):
        return None

    return user


async def generate_access_token(
    user: UserDB,
) -> dict:
    """Service for generating access token."""
    data = {"sub": str(user.id)}
    token = generate_token(data, ACCESS_TOKEN_EXPIRE_DAYS, SECRET_KEY)
    return {
        'access_token': token,
        'token_type': 'bearer',
    }
