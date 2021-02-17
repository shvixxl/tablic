"""Auth database module."""

from fastapi import Depends
from pydantic import EmailStr

from ..db.mongodb import MongoDB, get_db
from ..schemas.auth import UserDB, MongoModel
from ..config import MONGO_USER_COLLECTION

from .base import CRUDBase


class CRUDUser(CRUDBase):
    """Database adapter for auth module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection.create_index('email', unique=True)


    async def get_by_email(self, email: EmailStr) -> MongoModel:
        """Retrieves User from database by Email."""
        user = await self.collection.find_one({'email': email})
        return self.model(**user) if user else None


async def get_users() -> CRUDUser:
    """Return `CRUDUser` instance."""
    database = await get_db()
    return CRUDUser(database[MONGO_USER_COLLECTION], UserDB)
