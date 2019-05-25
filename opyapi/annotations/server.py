from __future__ import annotations
from . import Annotation


class Server(Annotation):
    def __init__(self, url: str, description: str = "", variables: list = None):
        self.variables = variables
        self.description = description
        self.url = url