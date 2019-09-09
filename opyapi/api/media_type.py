from typing import Any
from typing import Dict

from ..schema import Schema
from ..schema import String
from .annotation import read_annotation
from .doc_object import DocObject
from .resource import Resource


class MediaType(DocObject):
    """
    .. _Media Type Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#media-type-object
    TODO implement encoding objects support in later version
    """

    def __init__(self, media_type: str, schema: Schema, example: str = ""):
        self.schema = schema
        self.example = example
        self.media_type = media_type

    def to_doc(self) -> dict:

        try:
            id = read_annotation(self.schema).id
            schema = {"$ref": f"#/components/schemas/{id}"}
        except ValueError:
            schema = self.schema.to_doc()

        doc: Dict[str, Any] = {self.media_type: {"schema": schema}}
        if self.example:
            doc[self.media_type]["example"] = self.example

        return doc


class JsonContent(MediaType):
    def __init__(self, schema: Schema, example: str = ""):
        super().__init__("application/json", schema, example)


class XmlContent(MediaType):
    def __init__(self, schema: Schema, example: str = ""):
        super().__init__("text/xml", schema, example)


class TextContent(MediaType):
    def __init__(self, schema: Schema = None, example: str = ""):
        if not schema:
            schema = String()
        super().__init__("text/plain", schema, example)


__all__ = ["MediaType", "JsonContent", "XmlContent", "TextContent"]
