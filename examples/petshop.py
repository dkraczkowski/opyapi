from os import name

from opyapi import api
from opyapi.schema import Schema
from opyapi.schema import Type


@api.Server(url="asa", description="Server description that replaces doc")
class DevelopmentServer:
    """
    This doc will be ignored as description is set in decorator
    """
    pass


@api.Api(version="1.0.0", title="Pet Shop application", servers=[DevelopmentServer])
class PetShopApplication:
    pass


@api.Resource(title="Pet schema", schema=Schema(Type.OBJECT, required=["name", "age"]))
class Pet:
    """
    Description for the Pet resource
    """
    name: Schema(Type.STRING)
    age: Schema(Type.INTEGER) = None


@api.Operation(route="/pets/{id}", method="GET", responses={})
def get_pet(id: int):
    """
    Description for the pet operation
    """
    return Pet(name="Tom")


pet = Pet(name="Tom")

print(pet)
