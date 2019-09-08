from ...schema.validators import validators
from ..doc_object import DocObject


class License(DocObject):
    """
    Defines license information for the exposed API.

    .. _License Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#license-object
    """

    def __init__(self, name: str, url: str = ""):
        validators.url.validate(url)

        self.name = name
        self.url = url

    def to_doc(self):
        return {"name": self.name, "url": self.url}


__all__ = ["License"]
