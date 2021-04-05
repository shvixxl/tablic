"""Routes for chat module."""

from typing import List

from fastapi import APIRouter, Depends, status

from app import services
from app.api import deps
from app.crud import messages
from app.schemas import UserDB, TableDB, MessageIn, MessageOut

router = APIRouter(
    tags=['chat']
)


@router.get(
    '/{table_id}/messages',
    response_model=List[MessageOut],
    status_code=status.HTTP_201_CREATED,
)
async def get_messages(
    table: TableDB = Depends(deps.get_table),
) -> List[MessageOut]:
    """Get all messages from the chat of the table."""
    return await messages.get_by_table_id(table.id)


@router.post(
    '/{table_id}/messages',
    response_model=MessageOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_message(
    message: MessageIn,
    user: UserDB = Depends(deps.get_user),
    table: TableDB = Depends(deps.get_table),
) -> MessageOut:
    """Create new message for the chat of the table."""
    return await services.create_message(message, user, table)
