"""Test cases for user schema classes."""

import pytest

from pydantic import ValidationError

from app.schemas.auth.user import User
from app.schemas.auth import UserIn, UserOut, UserDB


def test_user(email):
    """Test base user model."""
    user = User(email=email)
    assert user.email == email


def test_user_validation():
    """Test base user model."""
    with pytest.raises(ValidationError) as error:
        User()
    assert 'email' in str(error)


def test_user_in(email, password):
    """Test user input model."""
    user = UserIn(email=email, password=password)
    assert user.password == password


def test_user_in_validation():
    """Test user input model valiation."""
    with pytest.raises(ValidationError) as error:
        UserIn()
    assert 'password' in str(error)


def test_user_out(object_id, email):
    """Test user output model."""
    user = UserOut(id=object_id, email=email)
    assert user.id == object_id

    user = UserOut(email=email)
    assert user.id is None


def test_user_db(object_id, email, password):
    """Test user database model."""
    user = UserDB(id=object_id, email=email, password_hash=password)

    assert user.id == object_id
    assert user.email == email
    assert user.password_hash == password


def test_user_db_from_mongo(object_id, email, password):
    """Test user database model from mongo query result."""
    mongo = {'_id': object_id, 'email': email, 'password_hash': password}
    user = UserDB(**mongo)

    assert user.id == object_id
    assert user.email == email
    assert user.password_hash == password


def test_user_db_mongo(object_id, email, password):
    """Test user database model to mongo."""
    user = UserDB(id=object_id, email=email, password_hash=password)
    mongo = user.mongo()

    assert mongo.get('_id') == object_id
    assert mongo.get('email') == email
    assert mongo.get('password_hash') == password
