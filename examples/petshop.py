from opyapi import api
from opyapi.api import Property
from dataclasses import dataclass


@api.Server(
    url="asa",
    description="Dupa"
)
class DevelopmentServer:
    pass


@api.Application(
    version="1.0.0",
    title="Pet Shop application",
    servers=[
        DevelopmentServer,
    ]
)
class PetShopApplication:
    pass


@api.Schema(title="Pet schema")
class Pet:
    name: Property()


app = PetShopApplication()

print(app)
