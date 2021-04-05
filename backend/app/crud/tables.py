"""Table CRUD."""

from app.schemas import TableDB

from .base import CRUDBase


class CRUDTables(CRUDBase):
    """CRUD for collection of tables."""


tables = CRUDTables(TableDB)
