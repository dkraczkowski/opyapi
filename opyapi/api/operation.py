from __future__ import annotations
from typing import List
from .annotation import Annotation
from .response import Response
from .parameter import Parameter
from ..application import Application


class Operation(Annotation):
    """
    .. _Open Api Operation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#operationObject
    """

    def __init__(
        self,
        route: str,
        method: str = "get",
        responses: List[Response] = [],
        summary: str = "",
        description: str = "",
        parameters: List[Parameter] = None,
        request=None,
        tags: list = None,
    ):
        self.route = route
        self.method = method
        self.summary = summary
        self.description = description
        self.parameters = parameters
        self.responses = responses
        self.request = request
        self.tags = tags

    def __call__(self, target):
        super().__call__(target)
        Application.add_operation(target)
