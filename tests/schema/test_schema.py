import datetime
from enum import Enum
from typing import AnyStr
from typing import Optional

import pytest

from opyapi.schema import Schema
from opyapi.schema import types
from opyapi.schema.errors import ValidationError


class ItemCategory(Enum):
    ELECTRONICS = "electronics"
    FOOD = "food"
    TOOLS = "tools"


class Item(Schema):
    """
    Some class description.
    Longer class description.
    """

    category: ItemCategory
    name: types.String(min_length=2, max_length=10)


class PetCategory(Enum):
    DOG = "dog"
    CAT = "cat"
    PARROT = "parrot"


class Pet(Schema, required=["name", "type"]):
    """
    Pet class title.
    Longer pet class description.
    """

    type: PetCategory  #: type description
    name: types.String(min_length=2, max_length=10)
    weight: types.Integer(minimum=1, maximum=100)
    created_at: types.String(string_format=types.StringFormat.DATETIME)
    age: Optional[int]


def test_schema():
    test_type = Optional[AnyStr]
    print(test_type)


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


def test_format_values():
    pet = Pet(type="dog", name="Pimpek", weight=20, created_at="2019-02-01 10:21:10")

    assert isinstance(pet.created_at, datetime.datetime)
