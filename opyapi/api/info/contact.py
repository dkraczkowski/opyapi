from ...schema.validators import validators
from ..doc_object import DocObject


class Contact(DocObject):
    """
    Defines contact information for the exposed API.

    .. _Contact Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#contact-object
    """

    def __init__(self, name: str, url: str = "", email: str = ""):
        validators.email.validate(email)
        validators.url.validate(url)

        self.name = name
        self.url = url
        self.email = email

    def to_doc(self):
        return {"name": self.name, "url": self.url, "email": self.email}


__all__ = ["Contact"]
