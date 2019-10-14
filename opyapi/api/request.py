from .api_doc import ApiDoc
from .media_type import MediaType


class Request(ApiDoc):
    def __init__(
        self, content: MediaType, description: str = "", required: bool = False
    ):
        self.content = content
        self.description = description
        self.required = required

    def to_doc(self) -> dict:
        doc = {"content": self.content.to_doc(), "required": self.required}
        if self.description:
            doc["description"] = self.description

        return doc


__all__ = ["Request"]
