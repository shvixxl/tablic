"""Module with templates of CRUD."""

from typing import TypeVar, Union, Optional

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

    async def get(self, object_id: Union[ObjectId, str]) -> Optional[Model]:
        """Returns object from database by `id`."""
        obj = await self.collection.find_one({'_id': ObjectId(object_id)})
        return self._serialize(obj)

    async def create(self, obj: Model) -> Model:
        """Creates new object in database."""
        data = obj.mongo(exclude_unset=True)
        result = await self.collection.insert_one(data)
        return self.model(**dict(obj.dict(), id=result.inserted_id))

    async def update(self, obj: Model) -> Model:
        """Updates an existing object in database."""
        data = obj.mongo()
        await self.collection.replace_one({'_id': obj.id}, data)
        return obj

    async def delete(self, object_id: Union[ObjectId, str]) -> None:
        """Deletes an existing object from database."""
        await self.collection.delete_one({'_id': ObjectId(object_id)})

    def _serialize(self, obj: dict) -> Optional[Model]:
        """Serializes object with `self.model` or returns `None`."""
        return self.model(**obj) or None
