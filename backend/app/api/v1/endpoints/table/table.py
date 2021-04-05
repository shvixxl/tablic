"""Routes for table module."""

from fastapi import APIRouter, Depends, status

from app import services
from app.api import deps
from app.schemas import UserDB, TableIn, TableOut, TableDB

router = APIRouter(
    tags=['table']
)


@router.get(
    '/{table_id}',
    response_model=TableOut,
    status_code=status.HTTP_200_OK,
)
async def get_table(
    table: TableDB = Depends(deps.get_table),
) -> TableOut:
    """Get user's table by id."""
    return table


@router.post(
    '/',
    response_model=TableOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_table(
    table: TableIn,
    user: UserDB = Depends(deps.get_user),
) -> None:
    """Create table."""
    return await services.create_table(table, user)
