from __future__ import annotations
from . import Annotation
from ..application import Application


class Api(Annotation):
    """
    Defines entry point for the application also stands as a entry point in open api documentation.

    .. _Open API Documentation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
    """

    def __init__(
        self,
        title: str,
        description: str = None,
        servers: list = None,
        version: str = "1.0.0",
    ):
        """
        :param title: Your api title
        :param servers: List of servers available for your api
        :param version: Semantic version number of your api
        """
        self.title = title
        self.servers = servers
        self.version = version
        self.description = description

    def __call__(self, target):
        super().__call__(target)
        return type(
            "Api" + target.__name__,
            (target, Application),
            {},
        )
