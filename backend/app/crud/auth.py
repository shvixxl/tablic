"""Auth database module."""

from pydantic import EmailStr

from ..config import MONGO_USER_COLLECTION
from ..schemas.auth import UserDB

from .base import CRUDBase


class CRUDUser(CRUDBase):
    """Database adapter for auth module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection.create_index('email', unique=True)


    async def get_by_email(self, email: EmailStr) -> UserDB:
        """Retrieves User from database by Email."""
        user = await self.collection.find_one({'email': email})
        return user


users = CRUDUser(MONGO_USER_COLLECTION, UserDB)
