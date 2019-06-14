import re
from copy import copy
from typing import Callable, Tuple, Union, Any, Optional

_ROUTE_REGEX = r"\{\s*(?P<var>[a-z_][a-z0-9_-]*)\s*\}"
_VAR_REGEX = "[^/]+"
_SUPPORTED_METHODS = ("get", "post", "put", "delete", "patch", "options", "head")


class Route:
    def __init__(self, route: str, **kwargs) -> None:
        self.route = route
        self._part_patterns = kwargs
        self._attribute_names = []
        self._pattern = None
        self._attributes = {}

    @property
    def pattern(self) -> str:
        if not self._pattern:
            self._parse()
        return self._pattern

    def _parse(self) -> None:
        def _parse_var(match):
            attribute = match.group(1)
            self._attribute_names.append(attribute)
            if attribute in self._part_patterns:
                return f"({self._part_patterns[attribute]})"
            return f"({_VAR_REGEX})"

        self._pattern = re.compile(
            "^" + re.sub(_ROUTE_REGEX, _parse_var, self.route, re.I | re.M) + "$",
            re.I | re.M,
        )

    def match(self, uri: str) -> Union[bool, "Route"]:
        matches = self.pattern.findall(uri)
        if not matches:
            return False

        if not self._attribute_names:
            return copy(self)

        if isinstance(matches[0], tuple):
            matches = matches[0]

        route = copy(self)
        match_index = 0
        for value in matches:
            route._attributes[self._attribute_names[match_index]] = value
            match_index += 1

        return route

    def __str__(self) -> str:
        return self.route

    def __bool__(self) -> bool:
        return True

    def __getitem__(self, key: str) -> str:
        return self._attributes[key]

    def __contains__(self, key: str) -> bool:
        return key in self._attributes

    def get(self, key: str, default: Optional[Any] = None):
        if key in self:
            return self[key]

        return default


class Router:
    def __init__(self) -> None:
        self._routes = {}
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

    def match(self, method: str, uri: str) -> Union[bool, Tuple[Route, Callable]]:
        for route in self._routes[method.lower()]:
            if route[0].match(uri):
                return route

        return False


__all__ = [Route, Router]
