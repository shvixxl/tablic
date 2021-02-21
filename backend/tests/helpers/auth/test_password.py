"""Test cases for auth module password helpers."""

from app.helpers.auth import generate_password_hash, check_password_hash


def test_generate_password_hash(password):
    """Test `generate_password_hash` function."""
    password_hash = generate_password_hash(password)
    assert password_hash is not None
    assert isinstance(password_hash, bytes)


def test_check_password_hash(faker, password):
    """Test `check_password_hash` function."""
    password_hash = generate_password_hash(password)
    wrong_password = faker.password()

    assert check_password_hash(password, password_hash)
    assert not check_password_hash(wrong_password, password_hash)
