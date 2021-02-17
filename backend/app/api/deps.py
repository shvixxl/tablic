"""API dependencies."""

from fastapi import Depends

from ..config import MONGO_USER_COLLECTION
from ..crud.auth import CRUDUser
from ..db.mongodb import MongoDB, db
from ..schemas.auth import UserDB


async def get_db() -> MongoDB:
    """Returns database instance."""
    return db.database


async def get_users(database: MongoDB = Depends(get_db)) -> CRUDUser:
    """Return users instance."""
    return CRUDUser(database[MONGO_USER_COLLECTION], UserDB)
