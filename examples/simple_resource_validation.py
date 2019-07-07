from opyapi.api import *
from opyapi import schema
from opyapi.http import HttpResponse


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


@Operation("/pets", method="post", request=Request(schema=Pet))
def create_pet(pet: Pet) -> HttpResponse:
    response = HttpResponse(headers={"Content-Type": "text/plain"})
    response.write(f"New pet name is: {pet.name}")

    return response


Application.run("development")
