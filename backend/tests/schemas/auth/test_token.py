"""Test cases for token schema classes."""

import pytest

from pydantic import ValidationError

from app.helpers.auth import generate_token
from app.schemas.auth import Token


def test_token(object_id, secret, time_delta):
    """Test token schema."""
    token_dict = {
        'access_token': generate_token(
            {'sub': str(object_id)},
            secret,
            time_delta,
        ),
        'token_type': 'bearer',
    }
    token_model = Token(**token_dict)

    assert token_model.access_token == token_dict.get('access_token')
    assert token_model.token_type == token_dict.get('token_type')


def test_token_validation():
    """Test token schema validation."""
    with pytest.raises(ValidationError) as error:
        Token()
    assert 'access_token' in str(error)
    assert 'token_type' in str(error)
