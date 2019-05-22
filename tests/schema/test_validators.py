import pytest

from opyapi.schema import validators


def test_type_validator():
    validator = validators.Type(int)
    assert validator.is_valid(12)


def test_integer_validator():
    validator = validators.Integer()
    assert validator.is_valid(10)
    assert not validator.is_valid("aa")


class TestA:
    attr_1 = "a"
    attr_2 = "b"


def test_class_attributes():
    t1 = TestA()
    t2 = TestA()
    t1.attr_1 = "c"

    a = 1
