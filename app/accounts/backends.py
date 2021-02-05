from django.contrib.auth.backends import BaseBackend

from .models import User


class EmailBackend(BaseBackend):
    """Backend to perform authentication via email"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')

        if username is None or password is None:
            return None

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            is_active = getattr(user, 'is_active', None)
            if user.check_password(password) and (is_active or is_active is None):
                return user

        return None
