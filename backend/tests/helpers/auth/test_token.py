"""Test cases for auth module token helpers."""

from datetime import datetime, timedelta

import jwt

from app.helpers.auth import generate_token, verify_token


def test_generate_token(uuid, secret, time_delta):
    """Test `generate_token` function."""
    token = generate_token({'sub': uuid}, secret, time_delta)

    assert token is not None
    assert isinstance(token, str)


def test_verify_token(uuid, secret, time_delta):
    """Test `verify_token` function."""

    token = generate_token({'sub': uuid}, secret, time_delta)
    payload = verify_token(token, secret)

    assert payload is not None
    assert isinstance(payload, dict)
    assert payload.get('sub') == uuid
    assert datetime.fromtimestamp(payload.get('exp')) > datetime.now()


def test_wrong_secret(faker, uuid, secret, time_delta):
    """Test `verify_token` with wrong secret."""

    wrong_secret = faker.password(32)

    token = generate_token({'sub': uuid}, secret, time_delta)
    payload = verify_token(token, wrong_secret)

    assert payload is None


def test_expired_token(faker, uuid, secret):
    """Test expired token."""

    time_delta = faker.time_delta(0) - timedelta(1)

    token = generate_token({'sub': uuid}, secret, time_delta)
    payload = verify_token(token, secret)

    assert payload is None


def test_token_headers(uuid, secret, time_delta):
    """Test token headers."""

    token = generate_token({'sub': uuid}, secret, time_delta)
    headers = jwt.get_unverified_header(token)

    assert headers.get('alg') == 'HS256'
    assert headers.get('typ') == 'JWT'
