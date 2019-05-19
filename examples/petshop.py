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

    id: Schema(Type.STRING, read_only=True, description="")
    name: Schema(Type.STRING)
    age: Schema(Type.INTEGER) = None


@api.Operation(
    method=api.OperationMethod.POST,
    route="/pets",
    request=api.Request(Pet),
    responses=[api.Response(Pet)],
)
def create_pet():
    return Pet(name="Tom")


@api.Operation(
    route="/pets/{id}",
    method=api.OperationMethod.GET,
    request=api.Request(Schema(Type.OBJECT, properties={})),
    responses={},
)
def get_pet(id: int):
    """
    Description for the pet operation
    """
    return Pet(name="Tom")

