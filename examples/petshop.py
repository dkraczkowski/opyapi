from opyapi.annotations import Api, Resource, Operation
from opyapi.schema.types import Enum, String, Integer, Number, Reference
from opyapi.schema.types.string import Format


@Api(
    version="1.0.0",
    title="Pet shop API"
)
class Application:
    pass


@Resource(
    title="Money resource"
)
class Money:
    currency: Enum("GBP", "USD", "PLN")
    amount: Number()


@Resource(
    title="Pet resource"
)
class Pet:
    id: String(string_format=Format.UUID)
    name: String(min_length=2)
    category: Enum("cats", "dogs", "parrots", "fishes")
    age: Integer(minimum=0, maximum=100)
    price: Reference(Money)


@Operation(
    "/pets/{id}",
    method="get"
)
def get_pet():
    pass
