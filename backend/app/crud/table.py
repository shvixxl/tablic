"""Table CRUD."""

from app.schemas.table import TableDB

from .base import CRUDBase


class CRUDTable(CRUDBase):
    """CRUD for collection of tables."""


tables = CRUDTable(TableDB)
