"""API v1."""

from fastapi import APIRouter

from .endpoints import auth, table, user

router = APIRouter()
router.include_router(auth.router, prefix='/auth')
router.include_router(user.router, prefix='/users')
router.include_router(table.router, prefix='/tables')
