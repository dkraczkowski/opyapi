from typing import Union
from ..schema import Schema


class Request:
    def __init__(self, schema: object, description: str = "") -> None:
        self.description = description
        self.schema = schema
