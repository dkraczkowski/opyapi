from typing import Callable

import bjoern

from .http import HttpRequest, HttpResponse, Router
from .controller import resolve_arguments


def _handle_callback(callback: Callable, args: list) -> HttpResponse:
    response = HttpResponse(200, {"Content-Type": "text/plain"})
    response.write("OK")
    return response


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

    def __call__(self, env: dict, start: Callable):
        request = HttpRequest.from_wsgi(env)
        result = self.router.match(request.method, request.path)
        if not result:
            start("404 Not Found", [("Content-Type", "text/plain")])
            return b""
        callback = result[1]
        response = _handle_callback(
            callback, resolve_arguments(callback, result[0], request)
        )

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
