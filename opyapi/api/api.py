from __future__ import annotations
from . import Annotation
from .annotation import _ANNOTATIONS


class Api(Annotation):
    """
    Defines entry point for the application also stands as a entry point in open api documentation.

    .. _Open API Documentation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
    """

    def __init__(self, title: str, servers: list, version: str = "1.0.0"):
        """
        :param title: Your api title
        :param servers: List of servers available for your api
        :param version: Semantic version number of your api
        """
        self.title = title
        self.servers = servers
        self.version = version

    def __call__(self, target):
        """
        :param target: annotated class or method
        :return: returns the target instance with applied api annotations
        """
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, [])
        target.__dict__[_ANNOTATIONS].append(self)
        setattr(Api, "__opyapi_application__", target)
        return target
