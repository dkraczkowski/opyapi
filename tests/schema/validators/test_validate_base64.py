from base64 import b64encode

import pytest

from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate_base64


@pytest.mark.parametrize("value", [
    b64encode(b"asa"),
    b64encode(b"another"),
])
def test_valid_values(value: str):
    validate_base64(value)


@pytest.mark.parametrize("value", [
    "asa",
    "another",
])
def test_invalid_values(value: str):
    with pytest.raises(ValidationError):
        validate_base64(value)
