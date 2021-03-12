"""Pytest fixtures."""

# pylint: disable=redefined-outer-name

from typing import Generator

import pytest
from bson.objectid import ObjectId
from httpx import AsyncClient

from app.main import app


@pytest.fixture
async def client() -> Generator:
    """`AsyncClient` instance."""
    async with AsyncClient(app=app) as client:
        yield client


@pytest.fixture
def secret(faker) -> str:
    """Random secret key."""
    return faker.password(32)


@pytest.fixture
def email(faker):
    """Random email address."""
    return faker.email()


@pytest.fixture
def password(faker):
    """Random password."""
    return faker.password(16)


@pytest.fixture
def time_delta(faker):
    """Time delta."""
    return faker.time_delta(1)


@pytest.fixture
def object_id():
    """Random uuid."""
    return ObjectId()
