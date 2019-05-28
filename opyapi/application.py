from __future__ import annotations
from typing import Callable
from .http import Request
import bjoern


class Application:
    """
    WSGI Application
    """

    def __init__(self):
        pass

    def __call__(self, env, start):
        request = Request(env)

        headers = request.headers
        start("200 OK", [("Content-Type", "text/plain")])
        return "Entry point!\n".encode(encoding="utf-8")

    @classmethod
    def start(
        cls, host: str = "0.0.0.0", port: int = 8080, runner: Callable = bjoern.run
    ):
        app = cls()
        runner(app, host, port)
