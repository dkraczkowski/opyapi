from typing import Callable

from bjoern import run

from .http_request import HttpRequest
from .middleware import Middleware
from .middleware_pipeline import MiddlewarePipeline


class Application:
    def __init__(self):
        self.middleware = MiddlewarePipeline()

    def boot(self):
        pass

    def use(self, middleware: Middleware):
        self.middleware.append(middleware)

    def __call__(self, env: dict, start: Callable):
        request = HttpRequest.from_wsgi(env)
        response = self.middleware(request)

        start(
            str(response.status_code),
            [(key, value) for key, value in response.headers.items()],
        )
        response.body.seek(0)
        return response.body

    def run(self, runner: Callable = run, host: str = "0.0.0.0", port: int = 80):
        self.boot()
        runner(self, host, port)


__all__ = ["Application"]
