"""Table services with bussines logic."""

from app.crud import users, tables
from app.schemas.auth import UserDB
from app.schemas.table import TableIn, TableDB, Player


async def create_table(
    table: TableIn,
    user: UserDB,
) -> TableDB:
    """Service for creating table and setting user as a creator."""
    players = [Player(**user.dict())]
    table_db = TableDB(**table.dict(), players=players)

    created_table = await tables.create(table_db)

    user.tables.append(created_table.id)
    await users.update(user)

    return created_table
