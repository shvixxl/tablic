"""Table schemas."""

from typing import Optional, List

from pydantic import BaseModel

from ..base import MongoModel

from .player import PlayerOut


class Table(BaseModel):
    """Base Table schema."""
    name: str


class TableIn(Table):
    """Input Table schema."""


class TableOut(MongoModel, Table):
    """Output Table schema."""
    players: Optional[List[PlayerOut]] = []


class TableDB(TableOut):
    """Database Table schema."""
