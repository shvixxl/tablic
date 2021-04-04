"""API v1."""

from fastapi import APIRouter

from .endpoints import auth, table

router = APIRouter()
router.include_router(auth.router, prefix='/auth')
router.include_router(table.router, prefix='/tables')
