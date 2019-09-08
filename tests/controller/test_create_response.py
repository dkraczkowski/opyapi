import pytest

from opyapi.controller import transform_object
from opyapi.schema import *


user_schema = Object(
    properties={
        "name": String(),
        "age": Integer(),
        "email": String(string_format=StringFormat.EMAIL),
    }
)


class TestUser:
    def __init__(self):
        pass


def test_transform_object_with_missing_property():
    bob = TestUser()
    bob.name = "Bob"
    bob.email = "bob@hasemail.com"
    bob.age = 15

    result = transform_object(bob, {"name": 1, "age": 1, "email": 1}, user_schema)

    assert {"name": "Bob", "email": "bob@hasemail.com", "age": 15} == result


def test_fail_when_property_not_mapped():
    bob = TestUser()
    bob.name = "Bob"
    bob.email = "bob@hasemail.com"
    bob.age = 15

    with pytest.raises(ValueError):
        transform_object(bob, {"name": 1, "email": 1}, user_schema)


def test_fail_when_invalid_mapping():
    bob = TestUser()
    bob.name = "Bob"
    bob.email = "bob@hasemail.com"
    bob.age = 15

    with pytest.raises(ValueError):
        transform_object(bob, {"name": 1, "age": 2, "email": 1}, user_schema)
