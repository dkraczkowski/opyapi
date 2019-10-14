from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

from opyapi.http.errors import NotFoundError
from .route import Route

_SUPPORTED_METHODS = ("get", "post", "put", "delete", "patch", "options", "head")


class Router:
    def __init__(self):
        self._routes: Dict[str, List] = {}
        for method in _SUPPORTED_METHODS:
            self._routes[method] = []

    def add_route(
        self, method: str, route: Union[str, "Route"], handler: Callable
    ) -> None:
        if isinstance(route, str):
            route = Route(route)

        assert isinstance(
            route, Route
        ), "Passed route must be either string or instance of Route"
        self._routes[str(method).lower()].append((route, handler))

    def match(self, method: str, uri: str) -> Tuple[Route, Callable]:
        for route in self._routes[method.lower()]:
            if route[0].match(uri):
                return route

        raise NotFoundError(f"Could not match any resource matching {uri} uri")


__all__ = ["Router"]
