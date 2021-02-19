"""API dependencies."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from ..config import USER_COLLECTION_NAME, SECRET_KEY
from ..crud.auth import CRUDUser
from ..db.mongodb import MongoDB, db
from ..schemas.auth import UserDB
from ..helpers.auth import verify_token

oauth2 = OAuth2PasswordBearer(
    tokenUrl='/api/v1/auth/login'
)

async def get_db() -> MongoDB:
    """Returns database instance."""
    return db.database


async def get_users(database: MongoDB = Depends(get_db)) -> CRUDUser:
    """Return users instance."""
    return CRUDUser(database[USER_COLLECTION_NAME], UserDB)


async def get_current_user(
    token: str = Depends(oauth2),
    users: CRUDUser = Depends(get_users)
) -> UserDB:
    """Validates token and returns user."""
    payload = verify_token(token, SECRET_KEY)
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
