"""Test cases for base schema classes."""

import pytest

from bson.objectid import ObjectId

from app.schemas.base import MongoId, MongoModel


def test_mongo_id(object_id):
    """Test `MongoId` type."""
    for validator in MongoId.__get_validators__():
        validated_id = validator(object_id)

        assert isinstance(validated_id, ObjectId)
        assert validated_id == object_id


@pytest.mark.parametrize('invalid_id', [1, '1'])
def test_mongo_id_validating(invalid_id):
    """Test `MongoId` validating."""
    for validator in MongoId.__get_validators__():
        with pytest.raises(ValueError):
            validator(invalid_id)


def test_init_mongo_model(object_id):
    """Test initalization of `MongoModel`."""
    obj = MongoModel(id=object_id)

    assert isinstance(obj.id, ObjectId)
    assert obj.id == object_id


def test_init_mongo_model_from_mongo(object_id):
    """Test initalization of `MongoModel` from mongo query result."""
    obj = MongoModel(_id=object_id)

    assert isinstance(obj.id, ObjectId)
    assert obj.id == object_id


def test_init_mongo_model_to_mongo(object_id):
    """Test `MongoModel` to mongo converting."""
    obj = MongoModel(id=object_id)
    mongo = obj.mongo()

    mongo_id = mongo.get('_id')

    assert isinstance(mongo_id, ObjectId)
    assert mongo_id == object_id
