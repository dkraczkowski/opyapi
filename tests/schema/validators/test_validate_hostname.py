import pytest

from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate_hostname


@pytest.mark.parametrize("input", ["google.com", "test.foo.bar", "localhost"])
def test_validate_valid_hostname(input: str):
    assert validate_hostname(input) is None


@pytest.mark.parametrize("input", ["!jkfd.com", "@mfd.com", "jkfd@jkfdkd.com"])
def test_validate_invalid_hostname(input: str):
    with pytest.raises(ValidationError):
        validate_hostname(input)
