"""Test cases for auth exceptions."""

from app.exceptions.auth import AuthError, UserAlreadyExists, UserNotExists


def test_auth_error():
    """Test `AuthError` exception."""
    assert issubclass(AuthError, Exception)


def test_user_already_exists():
    """Test `UserAlreadyExists` exception."""
    assert issubclass(UserAlreadyExists, AuthError)


def test_user_not_exists():
    """Test `UserNotExists` exception."""
    assert issubclass(UserNotExists, AuthError)
