"""Module with templates of CRUD."""

from typing import TypeVar

from motor.motor_asyncio import AsyncIOMotorCollection
from bson.objectid import ObjectId

from ..schemas.base import MongoModel

Model = TypeVar('Model', bound=MongoModel)


class CRUDBase:
    """Base CRUD for using with MongoDB."""

    collection: AsyncIOMotorCollection
    model: Model

    def __init__(self, collection: AsyncIOMotorCollection, model: Model):
        self.collection = collection
        self.model = model

    async def get(self, object_id: ObjectId) -> Model:
        """Gets object by `id` from database."""
        obj = await self.collection.find_one({'_id': object_id})
        return self.model(**obj) if obj else None

    async def create(self, obj: Model) -> Model:
        """Creates new object in database."""
        await self.collection.insert_one(obj.mongo(exclude_unset=True))
        return obj

    async def update(self, obj: Model) -> Model:
        """Updates an existing object in database."""
        await self.collection.replace_one({'_id': obj.id}, obj.mongo())
        return obj

    async def delete(self, obj: Model) -> None:
        """Delete an existing object from database."""
        await self.collection.delete_one({'_id': obj.id})
