"""Routes for auth module."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ....crud.auth import CRUDUser
from ....exceptions import UserAlreadyExists
from ....schemas.auth import UserIn, UserOut, Token
from ....services.auth import (
    create_user,
    authenticate_user,
    generate_access_token,
)

from ...deps import get_users

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
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
async def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    users: CRUDUser = Depends(get_users)
) -> Token:
    """User authentication."""
    user = await authenticate_user(credentials, users)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password.",
        )

    return await generate_access_token(user)
