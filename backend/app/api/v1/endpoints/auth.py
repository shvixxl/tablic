"""Routes for auth module."""

from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ....db.mongodb import get_db
from ....crud.auth import CRUDUser, get_users
from ....schemas.auth import UserIn, UserOut
from ....services.auth import create_user, authenticate_user
from ....exceptions import UserAlreadyExists

router = APIRouter(
    tags=['auth'],
)


@router.post(
    '/register',
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user: UserIn,
    users: CRUDUser = Depends(get_users)
) -> UserOut:
    """User registration."""
    try:
        created_user = await create_user(user, users)
    except UserAlreadyExists as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists.",
        ) from error

    return created_user


@router.post(
    '/login',
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
)
async def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    users: CRUDUser = Depends(get_users)
) -> UserOut:
    """User authentication."""
    user = await authenticate_user(credentials, users)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password."
        )

    return user
