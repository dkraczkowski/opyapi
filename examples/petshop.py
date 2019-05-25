from opyapi import annotations
from opyapi.schema import Schema
from opyapi import Application
from opyapi.schema import types


@annotations.Server(url="asa", description="Server description that replaces doc")
class DevelopmentServer:
    """
    This doc will be ignored as description is set in decorator
    """

    pass


@annotations.Api(version="1.0.0", title="Pet Shop application", servers=[DevelopmentServer])
class PetShopApplication:
    pass


@annotations.Resource(title="Pets favourite")
class Favourite:
    name: Schema(types.String)


@annotations.Resource(title="Pet schema", required=["name", "age"])
class Pet:
    """
    Description for the Pet resource
    """

    id: Schema(types.String, read_only=True)
    name: Schema(types.String)
    age: Schema(types.Integer) = None
    favourites: Schema(types.Object, all_of=)


@annotations.Operation(
    method=annotations.OperationMethod.POST,
    route="/pets",
    request=annotations.Request(Pet),
    responses=[annotations.Response(Pet)],
)
def create_pet(pet: Pet):
    return pet


@annotations.Operation(route="/pets/{id}", method=annotations.OperationMethod.GET, responses={})
def get_pet(id: int):
    """
    Description for the pet operation
    """
    return Pet(name="Tom")


Application.start()
