import pytest

from opyapi.exceptions import ValidationError
from opyapi.schema.types import Enum


def test_can_instantiate():
    test_instance = Enum("some", "accepted", "values")
    assert test_instance.allowed_values == ("some", "accepted", "values")


@pytest.mark.parametrize("value", ("some", "accepted", "values"))
def test_validate_pass(value):
    validator = Enum("some", "accepted", "values")
    assert validator.validate(value) == value


@pytest.mark.parametrize("value", ("invalid", "not", "blah"))
def test_validate_pass(value):
    validator = Enum("some", "accepted", "values")
    with pytest.raises(ValidationError):
        validator.validate(value)
