from opyapi.api import *
from opyapi import schema
import json


@Server(id="development", host="localhost", port=8080)
class DevelopmentServer:
    pass


@OpenApi(version="1.0.0", title="Pet shop API", servers=[DevelopmentServer])
class Application:
    pass


@Resource(title="Pet resource")
class Pet:
    id: schema.Integer(read_only=True)
    name: schema.String()
    category: schema.String()
    tags: schema.Array(items=schema.String())
    status: schema.Enum("available", "pending", "sold")


@Operation(
    "/pets", method="post", request=Request(schema=Pet), responses=[Response(Pet)]
)
def create_pet(pet: Pet):
    return 200, pet


Application.run("development")
