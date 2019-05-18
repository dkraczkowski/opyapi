from opyapi import api
from opyapi.schema import Schema
from opyapi.schema import Property


@api.Server(url="asa", description="Dupa")
class DevelopmentServer:
    pass


@api.Api(version="1.0.0", title="Pet Shop application", servers=[DevelopmentServer])
class PetShopApplication:
    pass


@api.Resource(title="Pet schema", schema=Schema({
    "name": Property(int)
}))
class Pet:
    name: Property(int)


app = PetShopApplication()

print(app)
