"""App configuration"""

from datetime import timedelta
from typing import Optional, List

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

    DB_HOST: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str

    DB_URI: Optional[AnyUrl] = None

    @validator('DB_URI', pre=True)
    def assemble_db_uri(cls, value: Optional[str], values: dict) -> str:
        """Assebles database URI."""
        if isinstance(value, str):
            return value
        return 'mongodb://{username}:{password}@{host}:{port}'.format(
            username=values.get('DB_USERNAME'),
            password=values.get('DB_PASSWORD'),
            host=values.get('DB_HOST'),
            port=values.get('DB_PORT'),
        )

    USER_COLLECTION_NAME: Optional[str] = 'users'

    class Config(BaseConfig):
        """Settings config class."""
        case_sensitive = True


settings = Settings()
