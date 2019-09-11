import pytest

from opyapi.api import Resource
from opyapi.schema import Integer
from opyapi.schema import String
from opyapi.schema import StringFormat


class TestUser:
    def __init__(self):
        pass


class TestUser2:
    def __init__(self):
        pass


@Resource(title="User schema", mapping={TestUser: {"name": 1, "age": 1, "email": 1}})
class UserObject:
    name: String()
    age: Integer()
    email: String(string_format=StringFormat.EMAIL)


def test_transform_object_with_missing_property():
    bob = TestUser()
    bob.name = "Bob"
    bob.email = "bob@hasemail.com"
    bob.age = 15
    result = UserObject.create_from(bob)

    assert {"name": "Bob", "email": "bob@hasemail.com", "age": 15} == result.to_dict()


def test_fail_when_invalid_mapping():
    bob = TestUser2()
    bob.name = "Bob"
    bob.email = "bob@hasemail.com"
    bob.age = 15

    with pytest.raises(ValueError):
        UserObject.create_from(bob)
