"""Test cases for mongodb module."""

import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.db.mongodb import MongoDB
from app.config import settings

@pytest.mark.asyncio
async def test_init_db():
    """Test initialization of database."""
    database = MongoDB()

    assert database.client is None
    assert database.database is None

@pytest.mark.asyncio
async def test_connection():
    """Test connection to the database."""
    database = MongoDB()

    await database.connect_to_database(settings.DB_URI)

    assert isinstance(database.client, AsyncIOMotorClient)
    assert database.client.PORT == settings.DB_PORT

    assert isinstance(database.database, AsyncIOMotorDatabase)
    assert database.database.name == settings.DB_NAME

    await database.close_database_connection()
