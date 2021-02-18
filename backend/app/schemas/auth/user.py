"""User schemas."""

from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from ..base import MongoModel


class User(MongoModel):
    """Base User scheme."""
    email: Optional[EmailStr] = None  # pylint: disable=E1136  # pylint/issues/3882


class UserIn(BaseModel):
    """Input User scheme."""
    email: EmailStr
    password: str


class UserOut(User):
    """Output User scheme."""


class UserDB(User):
    """Database User scheme."""
    password_hash: str
