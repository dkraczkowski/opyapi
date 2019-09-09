from typing import Optional
from typing import Type
from typing import TypeVar

from ..schema import validators
from .annotation import Annotation
from .annotation import bind_annotation
from .annotation import read_annotation
from .info import Contact
from .info import License

T = TypeVar("T")


class OpenApi(Annotation):
    servers: list = []
    version: str
    title: str
    description: str
    terms_of_service: str
    license: Optional[License]
    contact: Optional[Contact]
    operations: list = []
    resources: list = []

    """
    Defines entry point for the application also stands as a entry point in open api documentation.

    .. _Open API Documentation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md
    """

    def __init__(
        self,
        title: str,
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
        validators.sem_ver.validate(version)
        if terms_of_service:
            validators.url.validate(terms_of_service)
        OpenApi.version = version
        OpenApi.title = title
        OpenApi.description = description
        OpenApi.terms_of_service = terms_of_service
        OpenApi.contact = contact
        OpenApi.license = license

    def __call__(self, target: Type[T]) -> T:
        from ..application import Application

        new_type = type("Api" + target.__name__, (target, Application), {})
        bind_annotation(new_type, self)

        return new_type

    @classmethod
    def add_server(cls, handler, annotation: Annotation) -> None:
        bind_annotation(handler, annotation)
        cls.servers.append(handler)

    @classmethod
    def add_operation(cls, handler, annotation: Annotation) -> None:
        bind_annotation(handler, annotation)
        cls.operations.append(handler)

    @classmethod
    def add_resource(cls, handler, annotation: Annotation) -> None:
        if not annotation.id:
            annotation.id = handler.__name__
        bind_annotation(handler, annotation)
        cls.resources.append(handler)

    @classmethod
    def generate_doc(cls):
        result = {
            "openapi": "3.0.2",
            "info": {
                "title": cls.title,
                "version": cls.version,
                "description": cls.description,
            },
            "servers": [read_annotation(server).to_doc() for server in cls.servers],
        }
        if cls.terms_of_service:
            result["info"]["termsOfService"] = cls.terms_of_service

        if cls.contact:
            result["info"]["contact"] = cls.contact.to_doc()

        if cls.license:
            result["info"]["license"] = cls.contact.to_doc()

        if cls.operations:
            result["paths"] = {}

            for operation in cls.operations:
                path = read_annotation(operation).path
                method = read_annotation(operation).method
                if path not in result["paths"]:
                    result["paths"][path] = {}
                if method not in result["paths"][path]:
                    result["paths"][path][method] = {}

                result["paths"][path][method] = read_annotation(operation).to_doc()

        if cls.resources:
            result["components"] = {"schemas": {}}
            for resource in cls.resources:
                resource_annotation = read_annotation(resource)
                result["components"]["schemas"][
                    resource_annotation.id
                ] = resource.to_doc()

        return result


__all__ = ["OpenApi"]
