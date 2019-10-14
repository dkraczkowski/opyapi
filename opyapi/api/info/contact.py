from opyapi.schema.validators import validate_email
from opyapi.schema.validators import validate_url


class Contact:
    """
    Defines contact information for the exposed API.

    .. _Contact Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#contact-object
    """

    def __init__(self, name: str, url: str = "", email: str = ""):
        validate_email(email)
        validate_url(url)

        self.name = name
        self.url = url
        self.email = email


__all__ = ["Contact"]
