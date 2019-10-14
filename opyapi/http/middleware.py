from abc import ABC
from abc import abstractmethod

from .http_request import HttpRequest
from .http_response import HttpResponse
from .middleware_handler import MiddlewareHandler


class Middleware(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        pass


__all__ = ["Middleware"]
