from __future__ import annotations
from . import Annotation
from enum import Enum


class Method(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"
    OPTIONS = "options"
    HEAD = "head"


class Operation(Annotation):
    def __init__(
        self,
        route: str,
        method=None,
        summary: str = "",
        responses=None,
        request=None,
        tags: list = None,
    ):
        print("init")
