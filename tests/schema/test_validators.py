import pytest

from opyapi.schema import validators


def test_type_validator():
    validator = validators.Type(int)
    assert validator.is_valid(12)


def test_integer_validator():
    validator = validators.Integer()
    assert validator.is_valid(10)
    assert not validator.is_valid("aa")
