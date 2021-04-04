"""Routes for users module."""

from fastapi import APIRouter, Depends, status

from app.api import deps
from app.schemas import UserDB, UserOut

router = APIRouter(
    tags=['user']
)


@router.get(
    '/',
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def get_current_user(
    user: UserDB = Depends(deps.get_user),
) -> UserDB:
    """Get current user."""
    return user
