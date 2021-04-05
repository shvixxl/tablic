"""Chat services with business logic."""

import re

from app.schemas import MessageIn, MessageDB, UserDB, TableDB
from app.crud import messages
from app.helpers.chat.chat import parse_command


async def create_message(
    message: MessageIn,
    user: UserDB,
    table: TableDB,
) -> MessageDB:
    """Service for creating message."""
    new_text = await process_message(message.text)

    message_db = MessageDB(
        **dict(message.dict(), text=new_text),
        user_id=user.id,
        table_id=table.id
    )

    return await messages.create(message_db)


async def process_message(message: str) -> str:
    """Service for processing message."""
    command_regex = re.compile(r'\[\[(.*?)\]\]')

    commands = re.findall(command_regex, message)
    new_message = re.sub(command_regex, '{}', message)

    results = []
    for command in commands:
        results.append(parse_command(command))

    return new_message.format(*results)
