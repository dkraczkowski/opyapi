from __future__ import annotations
from .schema import Schema


class Response:
    """
    .. _Response implementation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#response-object
    """

    def __init__(self, code: int = 200, description: str = "", headers: list = None):
        self.headers = headers
        self.description = description
        self.code = code


class TextResponse(Response):
    def __init__(self, code: int = 200, description: str = "", headers: list = None):
        self.headers = headers
        self.description = description
        self.code = code


class JsonResponse(Response):
    def __init__(
        self,
        schema: Schema,
        code: int = 200,
        description: str = "",
        headers: list = None,
    ):
        pass
