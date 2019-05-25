from __future__ import annotations
from . import Annotation


class Operation(Annotation):
    """
    .. _Open Api Operation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#operationObject
    """
    def __init__(
        self,
        route: str,
        method=None,
        summary: str = "",
        description: str = "",
        responses=None,
        request=None,
        tags: list = None,
    ):
        print("init")
