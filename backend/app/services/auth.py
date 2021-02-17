"""Auth services with bussines logic."""

from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm

from ..helpers.auth.password import generate_password_hash, check_password_hash
from ..schemas.auth import UserIn, UserDB
from ..crud.auth import CRUDUser
from ..exceptions import UserAlreadyExists


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
