"""Base CRUD."""

from typing import Union, Optional

from motor.motor_asyncio import AsyncIOMotorCollection
from bson.objectid import ObjectId

from app.schemas.base import MongoModel


class CRUDBase:
    """Base CRUD for MongoDB."""

    def __init__(self, model: MongoModel):
        self.collection = None
        self.model = model

    async def init(self, collection: AsyncIOMotorCollection):
        """Connects CRUD and Database."""
        self.collection = collection

    async def get(self, object_id: Union[ObjectId, str]) -> Optional[MongoModel]:
        """Returns object from database by `id`."""
        obj = await self.collection.find_one({'_id': ObjectId(object_id)})
        return self._serialize(obj)

    async def create(self, obj: MongoModel) -> MongoModel:
        """Creates new object in database."""
        data = obj.mongo(exclude_unset=True)
        result = await self.collection.insert_one(data)
        return self.model(**dict(obj.dict(), id=result.inserted_id))

    async def update(self, obj: MongoModel) -> MongoModel:
        """Updates an existing object in database."""
        data = obj.mongo()
        await self.collection.replace_one({'_id': obj.id}, data)
        return obj

    async def delete(self, object_id: Union[ObjectId, str]) -> None:
        """Deletes an existing object from database."""
        await self.collection.delete_one({'_id': ObjectId(object_id)})

    def _serialize(self, obj: dict) -> Optional[MongoModel]:
        """Serializes object with `self.model` or returns `None`."""
        return self.model(**obj) if obj else None
