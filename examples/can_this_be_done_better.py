from opyapi import schema


class TypeDescriptor:
    def __init__(self, origin, params, *, name=None):
        self.__origin__ = origin
        self.__params__ = params
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        result = self.__origin__(*args, **kwargs)
        return result


class TypeDescriptorFactory:
    def __init__(self, name):
        self.__name__ = name

    def __getitem__(self, parameters):
        return TypeDescriptor(self, parameters)


class Decorator:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return args[0]


class Resource(Decorator):
    pass


class Get(Decorator):
    pass


class OpenApi(Decorator):
    def Resource(self):
        return Resource

    def Get(self):
        return Get


PathParameter = TypeDescriptorFactory("PathParameter")
JsonContent = TypeDescriptorFactory("JsonContent")
Responses = TypeDescriptorFactory("Responses")
Header = TypeDescriptorFactory("Header")


def authenticate(*args):
    pass


@OpenApi(
    version="1.0.0",
    title="Pet shop API"
)
class Application:
    pass


@Resource()
class Pet:
    id: schema.Integer(read_only=True)
    name: schema.String()
    category: schema.String()
    tags: schema.Array(schema.String())
    status: schema.Enum("available", "pending", "sold")


@Get("/pets/{id}")
def get_pet(id: PathParameter[int]) -> JsonContent[Pet]:
    pet = Pet(
        id,
        name="Boo",
        category="hamster",
        tags=["hamsters", "small"],
        status="available",
    )

    return pet


Application.run("development")
