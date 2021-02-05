from .models import User


def create_user(email: str, password: str, commit: bool=True):
    """Create new User from data"""

    user = User.objects.create_user(email, password)

    if commit:
        user.save()

    return user
