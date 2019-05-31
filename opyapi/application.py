from __future__ import annotations
from typing import Callable
import bjoern


class Application:
    """
    WSGI Application
    """

    def __init__(self, env, start):
        self._env = env
        self._start = start

    def __iter__(self):
        self._start("200 OK", [("Content-Type", "text/plain")])
        yield str.encode("Entry point!\n")

    @classmethod
    def start(
        cls, host: str = "0.0.0.0", port: int = 8080, runner: Callable = bjoern.run
    ):
        runner(cls, host, port)
