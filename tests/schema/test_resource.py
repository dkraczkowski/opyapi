import pytest

from opyapi.api import Resource
from opyapi.exceptions import ValidationError
from opyapi.schema.types import *


@Resource(title="Test item")
class Item:
    category: Enum("electronics", "food", "tools")
    name: String(min_length=2, max_length=10)


@Resource(title="Test pet", required=["name"])
class Pet:
    type: Enum("dog", "cat", "parrot")
    name: String(min_length=2, max_length=10)
    weight: Integer(minimum=1, maximum=100)


@pytest.mark.parametrize(
    "pet",
    (
        {"type": "dog", "name": "Pimpek", "weight": 20},
        {"type": "parrot", "name": "Heniek", "weight": 3},
    ),
)
def test_valid_pet(pet: dict):
    assert Pet(**pet)


@pytest.mark.parametrize(
    "pet",
    (
        {"type": "dog", "name": "Pimpek", "weight": 3001},
        {"type": "parrot", "name": "HeniekBylDobroPapugo", "weight": 3},
        {"type": "catel", "name": "Fluffy", "weight": 3},
    ),
)
def test_invalid_pet(pet: dict):
    with pytest.raises(ValidationError):
        Pet(**pet)


def test_to_doc():
    doc = Pet.to_doc()
    assert doc == {
        "type": "object",
        "required": ["name"],
        "properties": {
            "type": {"type": "string", "enum": ("dog", "cat", "parrot")},
            "name": {"type": "string", "minLength": 2, "maxLength": 10},
            "weight": {"type": "integer", "minimum": 1, "maximum": 100},
        },
    }

    doc = Item.to_doc()
    assert doc == {
        "type": "object",
        "properties": {
            "category": {"type": "string", "enum": ("electronics", "food", "tools")},
            "name": {"type": "string", "minLength": 2, "maxLength": 10},
        },
    }


class A:
    def __init__(self, default: list = []):
        self.list = default


def test_assign_value():
    a = A([1])
    b = A()
    c = A([1, 2])

    assert a.list == [1]
    assert b.list == []
    assert c.list == [1, 2]
