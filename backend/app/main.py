"""Main file of application"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .api.v1 import router
from .db.mongodb import db

app = FastAPI(
    title='Tablic',
    openapi_url='/api/v1/openapi.json'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
async def connect_to_database():
    """Event for establishing MongoDB connection."""
    await db.connect_to_database(settings.DB_URI)


@app.on_event('shutdown')
async def close_database_connection():
    """Event for closing MongoDB connection."""
    await db.close_database_connection()


app.include_router(router, prefix="/api/v1")
