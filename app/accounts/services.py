from .models import User


def create_user(username: str, email: str, password: str, commit: bool=True):
    """Create new User from data"""

    user = User.objects.create_user(username, email, password)

    if commit:
        user.save()

    return user
