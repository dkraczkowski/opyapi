import pytest

from opyapi.exceptions import ValidationError
from opyapi.schema.validators import SemVer


def test_can_instantiate():
    validator = SemVer()
    assert validator.validate("0.0.0")


@pytest.mark.parametrize(
    "value", ("1.0.0", "1.0.0-alpha", "1.0.0-alpha.1", "1.0.0-0.3.7", "1.0.0-x.7.z.92")
)
def test_valid_values(value: str):
    validator = SemVer()
    assert validator.validate(value) == value


@pytest.mark.parametrize(
    "value",
    (
        "1",
        "1.0",
        "1.0.0-.123",
        "1.0.0-...",
        "1.0.0-123.",
        "1.0.0-+",
        "1.0.0-+123",
        "1.0.0-",
    ),
)
def test_invalid_values(value: str):
    validator = SemVer()
    with pytest.raises(ValidationError):
        assert validator.validate(value) == value
