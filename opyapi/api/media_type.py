from .api_doc import ApiDoc
from .schema import generate_doc_from_schema
from .schema import Schema


class MediaType(ApiDoc):
    """
    .. _Media Type Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#media-type-object
    TODO implement encoding objects support in later version
    """

    def __init__(self, media_type: str, schema: Schema):
        self.schema = schema
        self.media_type = media_type

    def to_doc(self) -> dict:

        return {self.media_type: {"schema": generate_doc_from_schema(self.schema)}}


__all__ = ["MediaType"]
