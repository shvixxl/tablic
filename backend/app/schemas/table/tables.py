"""Table schemas."""

from typing import Optional, List

from pydantic import BaseModel

from app.schemas.base import MongoModel

from app.schemas.table.player import Player


class Table(BaseModel):
    """Base Table schema."""
    name: str


class TableIn(Table):
    """Input Table schema."""


class TableOut(MongoModel, Table):
    """Output Table schema."""
    players: Optional[List[Player]] = []


class TableDB(TableOut):
    """Database Table schema."""
