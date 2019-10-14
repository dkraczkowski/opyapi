from typing import List
from typing import Optional
from typing import TypeVar

from .annotation import Annotation
from .annotation import bind_annotation
from .info import Contact
from .info import License
from ..schema import validators

T = TypeVar("T")


class Api(Annotation):
    version: str
    title: str
    description: str
    terms_of_service: str
    license: Optional[License]
    contact: Optional[Contact]
    components: List[Annotation] = []

    """
    Defines entry point for the application also stands as a entry point in open api documentation.

    .. _Open API Documentation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
    """

    def __init__(
        self,
        title: str = "",
        version: str = "1.0.0",
        description: str = "",
        terms_of_service: str = "",
        license: Optional[License] = None,
        contact: Optional[Contact] = None,
    ):
        """
        :param title: Your api title
        :param version: Semantic version number of your api
        :param: description: A short description of the application
        :param: terms_of_service: A URL to the Terms of Service for the API. MUST be in the format of a URL.
        :param: license: The license information for the exposed API
        :param: contact: The contact information for exposed API
        """
        validators.validate_semver.validate(version)
        if terms_of_service:
            validators.validate_url.validate(terms_of_service)

        Api.components = []
        Api.version = version
        Api.title = title
        Api.description = description
        Api.terms_of_service = terms_of_service
        Api.contact = contact
        Api.license = license

    def __call__(self, target: T) -> T:

        new_type = type("Api" + target.__name__, target, {})  # type: ignore
        bind_annotation(new_type, self)

        return new_type

    @classmethod
    def register(cls, component: Annotation) -> None:
        Api.components.append(component)


__all__ = ["Api"]
