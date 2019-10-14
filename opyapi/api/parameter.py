from typing import Type as BaseType
from typing import Union

from ..schema import Type
from .api_doc import ApiDoc
from .schema import generate_doc_from_schema
from .schema import Schema


class Parameter(ApiDoc):
    """
    Implementation of Parameter Object

    .. _Parameter Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameters-object
    """

    def __init__(
        self,
        schema: Union[BaseType, Schema],
        description: str = "",
        required: bool = True,
        example: str = "",
        deprecated: bool = False,
        location: str = "path",
    ):
        self.name = ""
        self.description = description
        self.required = required
        if not isinstance(schema, Type):
            schema = Type.from_basic_type(schema)  # type: ignore
        self.schema = schema
        self.example = example
        self.deprecated = deprecated
        self.location = location
        self._location: str = "path"

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, location: str) -> None:
        assert location in (
            "query",
            "header",
            "path",
            "cookie",
        ), f"Invalid location `{location}` passed for parameters"
        self._location = location

    def to_doc(self) -> dict:
        doc = {
            "name": self.name,
            "in": self.location,
            "description": self.description,
            "required": self.required,
        }

        if self.deprecated:
            doc["deprecated"] = self.deprecated

        if self.schema:
            doc["schema"] = generate_doc_from_schema(self.schema)

        return doc


__all__ = ["Parameter"]
