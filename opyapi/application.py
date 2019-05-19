from __future__ import annotations
from typing import Callable
import bjoern
import re

_VARIABLE_REGEX = "/\
    \\s* ([a-zA-Z_][a-zA-Z0-9_-]*) \\s*\
    (?:\
        : \\s* ([^\\{\\}]*(?:{(?-1)}[^\\{\\}]*)*)\
    )?\
/"

_DISPATCH_REGEX = "'[^/]+'"


def parse_route(pattern: str):
    pattern.rsplit()


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
