from opyapi.schema.validators import validate_url


class License:
    """
    Defines license information for the exposed API.

    .. _License Object: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#license-object
    """

    def __init__(self, name: str, url: str = ""):
        validate_url(url)

        self.name = name
        self.url = url


__all__ = ["License"]
