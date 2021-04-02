"""Auth database module."""

from pydantic import EmailStr

from .base import CRUDBase, Model


class CRUDUser(CRUDBase):
    """Database adapter for auth module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection.create_index('email', unique=True)


    async def get_by_email(self, email: EmailStr) -> Model:
        """Retrieves User from database by Email."""
        user = await self.collection.find_one({'email': email})
        return self._serialize(user)
