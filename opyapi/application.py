from __future__ import annotations
from typing import Callable
import bjoern
from .http.request import Request


class Application:
    """
    WSGI Application
    """
    components: list = []

    @classmethod
    def add_component(cls, component):
        cls.components.append(component)

    def __init__(self):
        pass

    def __call__(self, env, start):
        request = Request.from_wsgi(env)
        start("200 OK", [("Content-Type", "text/plain")])
        return str.encode("Entry point!\n")

    @classmethod
    def run(
        cls, host: str = "0.0.0.0", port: int = 8080, runner: Callable = bjoern.run
    ):
        app = cls()
        runner(app, host, port)
