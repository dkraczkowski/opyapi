from typing import List, TypeVar, Type
from .annotation import Annotation
from .response import Response
from .parameter import Parameter
from ..application import Application

T = TypeVar("T")


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

    def __call__(self, target: Type[T]) -> T:
        super().__call__(target)
        Application.add_operation(target)

        return target
