from django.db.models import EmailField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model"""

    email = EmailField(
        max_length=254,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        },
    )
