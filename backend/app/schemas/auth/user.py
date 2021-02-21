"""User schemas."""

# pylint: disable=E1136  # pylint/issues/3882

from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from ..base import MongoId, MongoModel


class User(BaseModel):
    """Base User scheme."""
    email: EmailStr


class UserIn(User):
    """Input User scheme."""
    password: str


class UserOut(User):
    """Output User scheme."""
    id: Optional[MongoId] = None


class UserDB(MongoModel):
    """Database User scheme."""
    email: EmailStr
    password_hash: str
