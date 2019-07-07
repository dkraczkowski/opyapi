from typing import Type, TypeVar, Union

from . import Annotation
from ..application import Application

T = TypeVar("T")


class Server(Annotation):
    def __init__(
        self,
        id: str,
        host: str,
        port: int = 80,
        description: str = "",
        variables: Union[list, tuple] = (),
    ) -> None:
        self.id = id
        self.variables = variables
        self.description = description
        self.host = host
        self.port = port
        self.url = host + ":" + str(port)

    """
        Base class for all other classes that are used as decorators,
        responsible for binding open api api into user-land classes.
        """

    def __call__(self, target: Type[T]) -> T:
        super().__call__(target)
        Application.add_server(target)

        return target


__all__ = ["Server"]
