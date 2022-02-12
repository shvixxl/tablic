"""Application configuration module."""

# pylint: disable=no-self-argument,no-self-use  # pydantic validators

from typing import Optional, List, Union
from pathlib import Path
from datetime import timedelta

from pydantic import (
    BaseSettings,
    BaseConfig,
    AnyHttpUrl,
    AnyUrl,
    validator
)


class Settings(BaseSettings):
    """Application settings."""
    SECRET_KEY: str
    CORS_ORIGINS: List[AnyHttpUrl]
    ACCESS_TOKEN_EXPIRE_DAYS: timedelta

    @validator('ACCESS_TOKEN_EXPIRE_DAYS', pre=True)
    def expire_days_to_timedelta(cls, value: Optional[str]) -> timedelta:
        """Converts value of `ACCESS_TOKEN_EXPIRE_DAYS` to `timedelta`."""
        if isinstance(value, str):
            return timedelta(int(value))
        return value

    DB_URI: AnyUrl = 'mongodb://localhost:27017'

    USER_COLLECTION_NAME: Optional[str] = 'users'
    TABLE_COLLECTION_NAME: Optional[str] = 'tables'
    MESSAGE_COLLECTION_NAME: Optional[str] = 'messages'

    LOGGING_PATH: Optional[Path] = 'logs'
    LOGGING_FILENAME: Optional[str] = 'logs.json'

    @validator('LOGGING_PATH', pre=True)
    def assemble_logging_path(cls, value: Path, values: dict) -> Path:
        """"Adds filename to the path."""
        return Path(value) / values.get('LOGGING_FILENAME')

    LOGGING_FORMAT: Optional[str] = (
        '<level>{level: >8}</level> | '
        '<dim>{time:YYYY-MM-DD HH:mm:ss}</dim> | '
        '<normal>{message}</normal>'
    )

    LOGGING_LEVEL: Optional[Union[int, str]] = 20
    LOGGING_ROTATION: Optional[str] = '1 day'
    LOGGING_RETENTION: Optional[str] = '1 month'
    LOGGING_COMPRESSION: Optional[str] = 'tar.gz'

    class Config(BaseConfig):
        """Settings config class."""
        case_sensitive = True


settings = Settings()
