from .media_type import MediaType
from .doc_object import DocObject


class Request(DocObject):
    def __init__(
        self, content: MediaType, description: str = "", required: bool = True
    ):
        self.content = content
        self.description = description
        self.required = required

    def to_doc(self):
        doc = {"description": self.description, "content": self.content.to_doc()}

        if self.required:
            doc["required"] = self.required

        return doc


__all__ = ["Request"]
