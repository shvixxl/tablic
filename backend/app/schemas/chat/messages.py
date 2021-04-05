"""Message schemas."""

from datetime import datetime

from pydantic import BaseModel, Field

from ..base import MongoModel, MongoId


class Message(BaseModel):
    """Base Message schema."""
    text: str


class MessageIn(Message):
    """Input Message schema."""


class MessageOut(MongoModel, Message):
    """Output Message schema."""
    table_id: MongoId
    user_id: MongoId
    created_at: datetime


class MessageDB(MessageOut):
    """Database Message schema."""
    created_at: datetime = Field(default_factory=datetime.utcnow)
