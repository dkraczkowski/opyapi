from __future__ import annotations
from typing import Callable
import bjoern
from .http.request import Request
from .api.annotation import _ANNOTATION_PROPERTY


class Application:
    """
    WSGI Application
    """
    servers: list = []

    @classmethod
    def add_server(cls, server):
        cls.servers.append(server)

    @classmethod
    def get_server(cls, id: str):
        for component in cls.components:
            annotation = getattr(component, _ANNOTATION_PROPERTY)
            if isinstance()

    def __call__(self, env, start):
        request = Request.from_wsgi(env)
        start("200 OK", [("Content-Type", "text/plain")])
        return str.encode("Entry point!\n")

    @classmethod
    def run(
        cls, server_id: str, runner: Callable = bjoern.run
    ):
        app = cls()
        # runner(app, host, port)
