from opyapi import schema
from opyapi.api import *


@OpenApi(version="1.0.0", title="Pet shop API")
class Application:
    pass


@Server(id="development", host="localhost", port=8080, variables={})
class DevelopmentServer:
    pass


@Resource(title="Pet resource")
class Pet:
    id: schema.Integer(read_only=True)
    name: schema.String()
    category: schema.String()
    tags: schema.Array(items=schema.String())
    status: schema.Enum("available", "pending", "sold")


@GetOperation(
    "/pets/{id}",
    responses=[
        Response(
            content=JsonContent(Pet),
            status_code=200,
            headers={"fields": Header(schema.Array(schema.String()))},
        )
    ],
    parameters={"id": Parameter(schema.Integer())},
)
def get_pet(id: int):
    pet = Pet(
        id,
        name="Boo",
        category="hamster",
        tags=["hamsters", "small"],
        status="available",
    )

    return pet


@PostOperation(
    "/pets/",
    request=Request(
        content=JsonContent(Pet)
    ),
    responses=[
        Response(
            content=JsonContent(Pet),
            status_code=200
        )
    ]
)
def create_pet(pet: Pet):
    return pet


Application.run("development")
