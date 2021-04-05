"""Table module endpoints."""

from fastapi import APIRouter

from . import table, chat

router = APIRouter()
router.include_router(table.router)
router.include_router(chat.router)
