from opyapi.api import *
from opyapi.http import HttpRequest


@Server(id="development", host="localhost", port=8080)
class DevelopmentServer:
    pass


@OpenApi(version="1.0.0", title="Pet shop API", servers=[DevelopmentServer])
class Application:
    pass


@Operation("/pets/{id}", method="get")
def get_pet(request: HttpRequest):
    return f"Get pet with id {request.route['id']}"


Application.run("development")
