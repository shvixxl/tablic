"""Module with base classes for schemas."""

from typing import Any, Optional

from pydantic import BaseModel, BaseConfig
from bson.objectid import ObjectId, InvalidId  # pylint: disable=E0401  # vscode


class MongoId(str):
    """Field for Pydantic models for implementing Mongo's `_id` field."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """Validate value to be valid ObjectId."""
        try:
            return ObjectId(str(value))
        except InvalidId as error:
            raise ValueError('Not a valid ObjectId') from error


class MongoModel(BaseModel):
    """Pydantic BaseModel but with helpers for using with MongoDB."""

    id: Optional[MongoId] = None  # pylint: disable=E1136  # pylint/issues/3882

    class Config(BaseConfig):
        """Config for MongoModel."""
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str,
        }

    def __init__(self, **data: Any) -> None:
        """
        Extended Pydantic's `BaseModel.__init__` with parsing for
        Mongo's `_id` field.
        """
        object_id = data.pop('_id', None)
        if object_id:
            data.update(id=object_id)
        super().__init__(**data)

    def mongo(self, *args, **kwargs) -> dict:
        """Generates a dictionary for MongoDB."""
        parsed = self.dict(*args, **kwargs)
        parsed_id = parsed.pop('id', None)
        if parsed_id:
            parsed.setdefault('_id', parsed_id)
        return parsed
