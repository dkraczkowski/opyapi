from opyapi import api
from opyapi.schema import Schema
from opyapi import Application
from opyapi.schema import types


@api.Server(url="asa", description="Server description that replaces doc")
class DevelopmentServer:
    """
    This doc will be ignored as description is set in decorator
    """

    pass


@api.Api(version="1.0.0", title="Pet Shop application", servers=[DevelopmentServer])
class PetShopApplication:
    pass


@api.Resource(title="Pets favourite")
class Favourite:
    name: Schema(types.String)


@api.Resource(title="Pet schema", required=["name", "age"])
class Pet:
    """
    Description for the Pet resource
    """

    id: Schema(types.String, read_only=True)
    name: Schema(types.String)
    age: Schema(types.Integer) = None
    favourites: Schema(types.Object, all_of=)


@api.Operation(
    method=api.OperationMethod.POST,
    route="/pets",
    request=api.Request(Pet),
    responses=[api.Response(Pet)],
)
def create_pet(pet: Pet):
    return pet


@api.Operation(route="/pets/{id}", method=api.OperationMethod.GET, responses={})
def get_pet(id: int):
    """
    Description for the pet operation
    """
    return Pet(name="Tom")


Application.start()
