from typing import Any, Dict, List, Type, TypeVar

from . import Annotation
from .doc_object import DocObject
from .openapi import OpenApi

T = TypeVar("T")


class ServerVariable(DocObject):
    """
    An object representing a Server Variable for server URL template substitution.

    .. _Server Variable Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#server-variable-object
    """

    def __init__(self, default: str, enum: List[str] = None, description: str = ""):
        self.default = default
        self.description = description
        self.enum = enum

    def to_doc(self):
        doc = {"default": self.default}
        if self.description:
            doc["description"] = self.description
        if self.enum:
            doc["enum"] = self.enum
        return doc


class Server(Annotation):
    """
    Defines server for the exposed API.

    .. _Server Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#server-object
    """

    def __init__(
        self,
        id: str,
        host: str,
        port: int = 80,
        description: str = "",
        variables: Dict[str, ServerVariable] = {},
    ):
        self.id = id
        self.variables = variables
        self.description = description
        self.host = host
        self.port = port
        self.url = host + ":" + str(port)

    def __call__(self, target: Type[T]) -> T:
        OpenApi.add_server(target, self)
        return target

    def to_doc(self) -> dict:
        doc: Dict[str, Any] = {
            "description": self.description,
            "url": f"https://{self.host}:{self.port}",
        }

        if self.variables:
            doc["variables"] = {}
            for key, value in self.variables.items():
                doc["variables"][key] = value.to_doc()

        return doc


__all__ = ["Server", "ServerVariable"]
