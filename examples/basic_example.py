from opyapi.api import Api
from opyapi.api import get
from opyapi.api import JsonContent
from opyapi.api import parameters
from opyapi.schema import Schema
from opyapi.schema import types
from enum import Enum


@Api()
class Application:
    pass


class PetCategory(Enum):
    SNAKES = "snakes"
    CATS = "cats"
    DOGS = "dogs"


class Pet(Schema):
    """
    Pet Schema.
    """

    id: int
    name: types.String(max_length=24, min_length=2)
    description: str
    category: PetCategory


@get("/pets/{id}")
def get_pet(id: parameters.Path[int]) -> JsonContent[Pet]:
    """
    :param id: Pets id
    :return: Pet information
    """
    pet = Pet(id=id)
    return pet
