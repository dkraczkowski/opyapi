from typing import Optional, Union

from .resource import Resource
from ..schema import Schema


class Response:
    """
    .. _Response implementation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#response-object
    """

    def __init__(
        self,
        schema: Optional[Union[Resource, Schema]] = None,
        media_type: str = "",
        status_code: int = 200,
        description: str = "",
        headers: list = (),
        links: list = (),
    ) -> None:
        self.headers = headers
        self.description = description
        self.schema = schema
        self.status_code = status_code
        self.links = links
        self.media_type = media_type


class TextResponse(Response):
    def __init__(
        self,
        status_code: int = 200,
        description: str = "",
        headers: list = (),
        links: list = (),
    ) -> None:
        super().__init__(None, "plain/text", status_code, description, headers, links)


class JsonResponse(Response):
    def __init__(
        self,
        schema,
        status_code: int = 200,
        description: str = "",
        headers: list = (),
        links: list = (),
    ) -> None:
        super().__init__(
            schema, "application/json", status_code, description, headers, links
        )


__all__ = ["Response", "JsonResponse", "TextResponse"]
