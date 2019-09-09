from typing import Callable
from typing import Optional

import bjoern

from .api import OpenApi
from .api.annotation import read_annotation
from .api.server import Server
from .controller import create_response
from .controller import resolve_arguments
from .exceptions import HttpError
from .http import HttpRequest
from .http import HttpResponse
from .http import Router


class Application:
    """
    WSGI Application
    """

    servers: list = []
    operations: list = []
    resources: list = []
    router: Router
    suspended: bool = False

    def _boot(self):
        self.router = Router()
        for handler in OpenApi.operations:
            operation = getattr(handler, "__opyapi__")
            self.router.add_route(operation.method, operation.path, handler)

    @classmethod
    def suspend(cls):
        cls.suspended = True

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
    def run(cls, server_id: str, runner: Callable = bjoern.run) -> None:
        if (
            cls.suspended
        ):  # Application can be suspended from running if generation documentation happens
            return
        opyapi: OpenApi = read_annotation(cls)
        server: Optional[Callable] = None

        # Find server by id
        for server_handler in opyapi.servers:
            if read_annotation(server_handler).id == server_id:
                server = server_handler

        if server is None:
            raise ValueError(
                f"Server `{server_id}` was not recognized. "
                f"Are you sure you have decorated class with @Server(id='{server_id}' ...) decorator"
            )
        server_annotation: Server = read_annotation(server)
        app = cls()
        app._boot()
        runner(app, server_annotation.host, server_annotation.port)


__all__ = ["Application"]
