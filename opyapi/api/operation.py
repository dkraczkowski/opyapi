from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from ..schema import Schema
from .annotation import Annotation
from .openapi import OpenApi
from .parameter import Parameter
from .request import Request
from .response import Response

T = TypeVar("T")


class Operation(Annotation):
    def __init__(
            self,
            path: str,
            responses: List[Response],
            method: str = "get",
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request: Optional[Request] = None,
            tags: List[str] = [],
    ):
        self.path = path
        self.method = method
        self.summary = summary
        self.description = description
        self.responses = responses
        self.request = request
        self.tags = tags
        self.parameters: List[Parameter] = []

        if parameters:
            for key, parameter in parameters.items():
                if isinstance(parameter, Schema):
                    parameter = Parameter(parameter)
                parameter.location = "path"
                parameter.name = key
                self.parameters.append(parameter)

    """
    .. _Open Api Operation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#operationObject
    """

    def __call__(self, target: T) -> T:
        OpenApi.add_operation(target, self)
        return target

    def to_doc(self) -> dict:
        doc: Dict[Union[str, int], Any] = {
            "description": self.description,
            "summary": self.summary,
        }

        if self.tags:
            doc["tags"] = self.tags

        if self.parameters:
            doc["parameters"] = [parameter.to_doc() for parameter in self.parameters]

        doc["responses"] = {}

        for response in self.responses:
            key: Union[str, int] = response.status_code
            if response.is_default:
                key = "default"
            doc["responses"][key] = response.to_doc()

        if self.request:
            doc["requestBody"] = self.request.to_doc()

        return doc


class GetOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(GetOperation, self).__init__(
            path, responses, "get", summary, description, parameters, request, tags
        )


class PostOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(PostOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


class PutOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(PutOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


class PatchOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(PatchOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


class DeleteOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(DeleteOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


class HeadOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(HeadOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


class OptionsOperation(Operation):
    def __init__(
            self,
            path: str,
            responses: List[Response] = [],
            summary: str = "",
            description: str = "",
            parameters: Dict[str, Union[Parameter, Schema]] = {},
            request=None,
            tags: List[str] = [],
    ):
        super(OptionsOperation, self).__init__(
            path, responses, "post", summary, description, parameters, request, tags
        )


__all__ = [
    "Operation",
    "GetOperation",
    "PostOperation",
    "PutOperation",
    "PatchOperation",
    "DeleteOperation",
    "HeadOperation",
    "OptionsOperation",
]
