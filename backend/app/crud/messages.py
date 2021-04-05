"""Message CRUD."""

from typing import Union, Optional

from bson.objectid import ObjectId

from app.schemas import MessageDB

from .base import CRUDBase


class CRUDMessages(CRUDBase):
    """CRUD for collection of tables."""

    async def init(self, *args, **kwargs):
        await super().init(*args, **kwargs)
        self.collection.create_index('table_id')

    async def get_by_table_id(
        self,
        table_id: Union[ObjectId, str]
    ) -> Optional[MessageDB]:
        """Returns User from database by `email`."""
        return await self.query({'table_id': table_id})


messages = CRUDMessages(MessageDB)
