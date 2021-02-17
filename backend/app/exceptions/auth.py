"""Exceptions for auth module."""

class AuthError(Exception):
    """Base class for all auth exceptions."""


class UserAlreadyExists(AuthError):
    """User already exists in database."""


class UserNotExists(AuthError):
    """User doesn't exist in database."""
