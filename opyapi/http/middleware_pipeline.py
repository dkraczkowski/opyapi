from copy import deepcopy
from queue import Queue

from .http_request import HttpRequest
from .http_response import HttpResponse
from .middleware import Middleware
from .middleware_handler import MiddlewareHandler


class MiddlewareCursor(MiddlewareHandler):
    def __init__(self, queue: Queue, parent: MiddlewareHandler):
        self.queue: Queue = Queue()
        self.queue.queue = deepcopy(queue.queue)
        self.parent = parent

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if self.queue.empty():
            return self.parent(request)

        middleware: Middleware = self.queue.get()
        next = MiddlewareCursor(self.queue, self)
        return middleware.handle(request, next)


class EmptyPipelineHandler(MiddlewareHandler):
    def __call__(self, request: HttpRequest) -> HttpResponse:
        raise RuntimeError("Middleware pipe is empty.")


class MiddlewarePipeline(MiddlewareHandler, Middleware):
    def __init__(self, queue: Queue = Queue()):
        self.queue: Queue = Queue()
        self.queue.queue = deepcopy(queue.queue)

    def append(self, *middleware: Middleware) -> None:
        for item in middleware:
            self.queue.put(item)

    def __call__(self, request: HttpRequest) -> HttpResponse:
        return self.handle(request, EmptyPipelineHandler())

    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        return (MiddlewareCursor(self.queue, next)).__call__(request)


__all__ = ["MiddlewarePipeline"]
