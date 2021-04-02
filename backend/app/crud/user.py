"""Auth database module."""

from typing import Optional

from pydantic import EmailStr

from .base import CRUDBase, Model


class CRUDUser(CRUDBase):
    """Database adapter for auth module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection.create_index('email', unique=True)
        self.collection.create_index('username', unique=True)

    async def get_by_email(
        self,
        email: EmailStr
    ) -> Optional[Model]:
        """Returns User from database by `email`."""
        user = await self.collection.find_one({'email': email})
        return self._serialize(user)

    async def get_by_username(
        self,
        username: str
    ) -> Optional[Model]:
        """Returns User from database by `username`."""
        user = await self.collection.find_one({'username': username})
        return self._serialize(user)

    async def get_by_email_or_username(
        self,
        email: EmailStr,
        username: str
    ) -> Optional[Model]:
        """Returns User from database by `email` or `username`."""
        user = await self.collection.find_one({
            '$or': [
                {'email': email},
                {'username': username},
            ]
        })
        return self._serialize(user)
