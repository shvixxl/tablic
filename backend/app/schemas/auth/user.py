"""User schemas."""

from pydantic import BaseModel, EmailStr

from app.schemas.base import MongoModel


class User(BaseModel):
    """Base User schema."""
    email: EmailStr
    username: str


class UserIn(User):
    """Input User schema."""
    password: str


class UserOut(MongoModel, User):
    """Output User schema."""


class UserDB(MongoModel, User):
    """Database User schema."""
    password_hash: str
