from ..schema import Schema
from .doc_object import DocObject


class Parameter(DocObject):
    """
    Implementation of Parameter Object

    .. _Parameter Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameter-object
    """

    def __init__(
        self,
        schema: Schema,
        description: str = "",
        required: bool = True,
        example: str = "",
        deprecated: bool = False,
        location: str = "path",
    ):
        self.name = ""
        self.description = description
        self.required = required
        self.schema = schema
        self.example = example
        self.deprecated = deprecated
        self.location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        assert location in (
            "query",
            "header",
            "path",
            "cookie",
        ), f"Invalid location `{location}` passed for parameter"
        self._location = location

    def to_doc(self):
        doc = {
            "name": self.name,
            "in": self.location,
            "description": self.description,
            "required": self.required,
        }

        if self.deprecated:
            doc["deprecated"] = self.deprecated

        if self.schema:
            doc["schema"] = self.schema.to_doc()

        return doc


class Header(Parameter):
    def __init__(self, schema: Schema, description: str = ""):
        super().__init__(schema=schema, description=description, location="header")


__all__ = ["Parameter", "Header"]
