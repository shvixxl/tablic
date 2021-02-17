"""MongoDB module."""

import logging

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
)


class MongoDB:
    """Class for storing MongoDB connection"""
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None

    async def connect_to_database(self, uri: str):
        """Establish MongoDB connection."""
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(uri)
        self.database = self.client.main_db
        logging.info('Connected to MongoDB.')

    async def close_database_connection(self):
        """Close MongoDB connection."""
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")


db = MongoDB()
