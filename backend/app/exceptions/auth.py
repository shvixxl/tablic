"""Exceptions for auth module."""

class UserAlreadyExists(Exception):
    """User already exists in database."""


class UserNotExists(Exception):
    """User doesn't exist in database."""
