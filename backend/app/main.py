"""Main file of application"""

from fastapi import FastAPI

from app import config
from app.db.mongodb import db
from app.api.v1 import router

app = FastAPI()


@app.on_event('startup')
async def connect_to_database():
    """Event for establishing MongoDB connection."""
    await db.connect_to_database(config.MONGO_URI)


@app.on_event('shutdown')
async def close_database_connection():
    """Event for closing MongoDB connection."""
    await db.close_database_connection()


app.include_router(router, prefix="/api/v1")
