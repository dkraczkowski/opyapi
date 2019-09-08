from typing import Any
from typing import Dict

from .doc_object import DocObject
from .media_type import MediaType
from .parameter import Parameter


class Response(DocObject):
    """
    .. _Response implementation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#response-object
    """

    def __init__(
        self,
        content: MediaType,
        status_code: int = 200,
        description: str = "",
        headers: Dict[str, Parameter] = None,
        links: list = None,
        is_default: bool = False,
    ):
        self._headers: Dict[str, Parameter] = {}

        self.content = content
        self.description = description
        self.status_code = status_code
        self.links = links
        self.is_default = is_default
        if headers:
            self.headers = headers

    @property
    def headers(self) -> Dict[str, Parameter]:
        return self._headers

    @headers.setter
    def headers(self, value: Dict[str, Parameter]):
        for _, header in value.items():
            assert isinstance(header, Parameter)
        self._headers = value

    def to_doc(self) -> dict:
        doc: Dict[str, Any] = {
            "description": self.description,
            "content": self.content.to_doc(),
        }
        if self.headers:
            doc["headers"] = {}
            for name, header in self.headers.items():
                # Because open api lacks some consistency we cannot simply use to doc method here.
                doc["headers"][name] = {
                    "schema": header.schema.to_doc(),
                    "description": header.description,
                }
        return doc


__all__ = ["Response"]
