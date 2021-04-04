"""Main file of application"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import router
from app.config import settings
from app.logging import init_logger
from app.db.mongodb import db

logger = init_logger()

app = FastAPI(
    title='Tablic',
    openapi_url='/api',
    docs_url="/api/docs",
    redoc_url="/api/redoc",
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
