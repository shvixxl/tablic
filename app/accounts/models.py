from django.db.models import EmailField
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    """Custom User model"""

    objects = UserManager()

    username = None
    email = EmailField(
        max_length=254,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
