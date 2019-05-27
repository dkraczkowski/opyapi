from __future__ import annotations
from . import Annotation
from .annotation import _ANNOTATIONS


class Api(Annotation):
    """
    Defines entry point for the application also stands as a entry point in open annotations documentation.

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
        :param title: Your annotations title
        :param servers: List of servers available for your annotations
        :param version: Semantic version number of your annotations
        """
        self.title = title
        self.servers = servers
        self.version = version
        self.description = description

    def __call__(self, target):
        """
        :param target: annotated class or method
        :return: returns the target instance with applied annotations annotations
        """
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, [])
        target.__dict__[_ANNOTATIONS].append(self)
        return target
