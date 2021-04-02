"""Token schemas."""

from pydantic import BaseModel


class Token(BaseModel):
    """Token schema."""
    access_token: str
    token_type: str
