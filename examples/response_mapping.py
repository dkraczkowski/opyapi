from opyapi.api import *
from opyapi import schema


@Server(id="development", host="localhost", port=8080)
class DevelopmentServer:
    pass


@OpenApi(version="1.0.0", title="Pet shop API", servers=[DevelopmentServer])
class Application:
    pass


class DbPet:
    def __init__(self, name: str, pet_category: str):
        self.name = name
        self.pet_category = pet_category

    def get_tags(self):
        return ["test_tag"]


@Resource(
    title="Pet resource",
    mapping={
        DbPet: {
            "name": 1,
            "category": "pet_category",
            "tags": lambda pet: pet.get_tags(),
        }
    },
)
class PetDto:
    id: schema.Integer(read_only=True, nullable=True)
    name: schema.String()
    category: schema.String()
    tags: schema.Array(items=schema.String())
    status: schema.Enum("available", "pending", "sold", nullable=True)


@Operation(
    "/pets",
    method="post",
    request=Request(schema=PetDto),
    responses=[JsonResponse(PetDto, status_code=200)],
)
def create_pet(pet: PetDto):
    db_pet = DbPet(pet.name, pet.category)
    return 200, db_pet


Application.run("development")
