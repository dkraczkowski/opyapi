from abc import ABC
from abc import abstractmethod

from .http_request import HttpRequest
from .http_response import HttpResponse


class MiddlewareHandler(ABC):
    @abstractmethod
    def __call__(self, request: HttpRequest) -> HttpResponse:
        pass


__all__ = ["MiddlewareHandler"]
