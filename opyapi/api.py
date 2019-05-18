from __future__ import annotations
from .schema import Schema


_ANNOTATIONS = "__opyapi_annotations__"


class Annotation:
    """
    Base class for all other classes that are used as decorators,
    responsible for binding open api annotations into user-land classes.
    """
    def __call__(self, target):
        """
        :param target: annotated class or method
        :return: returns the target instance with applied api annotations
        """
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, [])
        target.__dict__[_ANNOTATIONS].append(self)
        return target


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


class Server(Annotation):
    def __init__(self, url: str, description: str = "", variables: list = []):
        print("init")


class Resource(Annotation):
    """
    Resource replaces Open Api Schema Objects to simplify documentation process.

    .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """
    def __init__(self, title: str, description: str = "", schema: Schema = None):
        print("init")

    def __call__(self, target):
        print(target.__dict__["__annotations__"])
        print(target.__dict__["age"])
        return target


class Operation(Annotation):
    def __init__(self, method=None, route=None, responses=None, request=None):
        print("init")
