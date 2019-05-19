from __future__ import annotations
from typing import Callable
import bjoern
import re

_ROUTE_REGEX = r"\{\s*(?P<var>[a-z_][a-z0-9_-]*)\s*\}"

_PARAMETER_REGEX = "'[^/]+'"


def parse_route(route: str, parameters: dict = None):
    def replace(match):
        print('replacing')
        print(match)
        pass

    parsed_pattern = re.findall(_ROUTE_REGEX, route, flags=re.MULTILINE|re.IGNORECASE)

    print(parsed_pattern)


class Router:
    pass


class Application:
    """
    WSGI Application
    """
    def __init__(self, env, start):
        self._env = env
        self._start = start

    def __iter__(self):
        self._start('200 OK', [('Content-Type', 'text/plain')])
        yield str.encode("Entry point!\n")

    @classmethod
    def start(cls, host: str = "0.0.0.0", port: int = 8080, runner: Callable = bjoern.run):
        runner(cls, host, port)
