import pytest

from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate_falsy


@pytest.mark.parametrize("input", [0.0, 0, "0", "false", False, "no", "nope", "n"])
def test_validate_valid_falsy_format(input: str):
    assert validate_falsy(input) is None


@pytest.mark.parametrize("input", [1, 1.0, "1", "any", "ni"])
def test_validate_invalid_email_format(input: str):
    with pytest.raises(ValidationError):
        validate_falsy(input)
