"""API dependencies."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import settings
from app.crud import users, tables
from app.helpers.auth import verify_token
from app.schemas import UserDB, TableDB, MongoId

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


async def get_table(
    table_id: MongoId,
    user: UserDB = Depends(get_user),
) -> TableDB:
    """
    Validates if the user is a member of the table and returns this table.
    """
    if not table_id in user.tables:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This table was not found among user's tables.",
        )

    table = await tables.get(table_id)

    return table
