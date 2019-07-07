from typing import Callable

import bjoern

from .controller import create_response, resolve_arguments
from .exceptions import HttpError
from .http import HttpRequest, HttpResponse, Router


class Application:
    """
    WSGI Application
    """

    servers: list = []
    operations: list = []
    resources: list = []
    router: Router

    def _boot(self):
        self.router = Router()
        for handler in self.operations:
            operation = handler.get_opyapi_annotation()
            self.router.add_route(operation.method, operation.route, handler)

    @classmethod
    def add_server(cls, server) -> None:
        cls.servers.append(server)

    @classmethod
    def add_operation(cls, operation) -> None:
        cls.operations.append(operation)

    @classmethod
    def add_resource(cls, resource) -> None:
        cls.resources.append(resource)

    @classmethod
    def get_server(cls, server_id: str):
        for server in cls.servers:
            annotation = server.get_opyapi_annotation()
            if annotation.id == server_id:
                return server

    def on_error(self, exception: Exception) -> HttpResponse:
        if isinstance(exception, HttpError):
            return exception

        return HttpError()

    def __call__(self, env: dict, start: Callable):
        request = HttpRequest.from_wsgi(env)
        try:
            result = self.router.match(request.method, request.path)
            route = result[0]
            controller = result[1]
            args = resolve_arguments(controller, route, request)
            response = create_response(controller, args)
        except Exception as e:
            response = self.on_error(e)

        if not isinstance(response, HttpResponse):
            response = HttpResponse(502)
            response.write("Failed to serve response.")

        start(
            str(response.status_code),
            [(key, value) for key, value in response.headers.items()],
        )
        response.body.seek(0)
        return response.body

    @classmethod
    def run(cls, server_id: str, runner: Callable = bjoern.run):
        server = cls.get_server(server_id)
        if server is None:
            raise ValueError(
                f"Server `{server_id}` was not recognized. "
                f"Are you sure you have decorated class with @Server(id='{server_id}' ...) decorator"
            )
        server_details = server.get_opyapi_annotation()
        app = cls()
        app._boot()
        runner(app, server_details.host, server_details.port)


__all__ = ["Application"]
