"""User schemas."""

# pylint: disable=E1136  # pylint/issues/3882

from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from ..base import MongoId, MongoModel


class User(BaseModel):
    """Base User schema."""
    email: EmailStr
    username: str


class UserIn(User):
    """Input User schema."""
    password: str


    """Output User schema."""
    id: Optional[MongoId] = None


    """Database User schema."""
    email: EmailStr
    password_hash: str
