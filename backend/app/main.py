"""Main file of application"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import crud
from app.db import db
from app.api.v1 import router
from app.config import settings
from app.logging import init_logger

logger = init_logger()

app = FastAPI(
    title='Tablic',
    openapi_url='/api',
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


@app.on_event('startup')
async def connect_to_database():
    """Event for establishing MongoDB connection."""
    await db.connect_to_database(settings.DB_URI)
    await crud.users.init(db.database[settings.USER_COLLECTION_NAME])
    await crud.tables.init(db.database[settings.TABLE_COLLECTION_NAME])
    await crud.messages.init(db.database[settings.MESSAGE_COLLECTION_NAME])


@app.on_event('shutdown')
async def close_database_connection():
    """Event for closing MongoDB connection."""
    await db.close_database_connection()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(router, prefix="/api/v1")
