"""User schemas."""

from typing import Optional, List

from pydantic import BaseModel, EmailStr

from app.schemas.base import MongoModel, MongoId


class User(BaseModel):
    """Base User schema."""
    email: EmailStr
    username: str


class UserIn(User):
    """Input User schema."""
    password: str


class UserOut(MongoModel, User):
    """Output User schema."""
    tables: Optional[List[MongoId]] = []


class UserDB(UserOut):
    """Database User schema."""
    password_hash: str
