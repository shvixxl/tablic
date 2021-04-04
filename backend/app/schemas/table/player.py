"""Player schemas."""

from pydantic import BaseModel

from app.schemas.base import MongoId


class Player(BaseModel):
    """Base Player schema."""
    id: MongoId


class PlayerIn(Player):
    """Input Player schema."""


class PlayerOut(Player):
    """Ouput Player schema."""


class PlayerDB(Player):
    """Database Player schema."""
