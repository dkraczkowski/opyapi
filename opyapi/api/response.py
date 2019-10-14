from .api_doc import ApiDoc
from .media_type import MediaType


class Response(ApiDoc):
    """
    Simplified response object implementation
    .. _Response object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#responseObject
    """

    def __init__(
        self, content: MediaType, status_code: int = 200, description: str = ""
    ):
        self.status_code = status_code
        self.description = description
        self.content = content

    def to_doc(self):
        return {"description": self.description, "content": self.content.to_doc()}


__all__ = ["Response"]
