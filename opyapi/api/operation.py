from typing import Any
from typing import Dict
from typing import List
from typing import TypeVar
from typing import Union
from typing import Optional

from .annotation import Annotation
from .annotation import bind_annotation
from .media_type import MediaType
from .parameter import Parameter
from .response import Response
from .request import Request
from .schema import Schema
from opyapi.utils import DocString
from .api import Api

T = TypeVar("T")


class Operation(Annotation):
    def __init__(
        self,
        path: str,
        method: str = "get",
        tags: List[str] = [],
        responses: Dict[int, MediaType] = {},
    ):
        self.path = path
        self.method = method
        self.summary = ""
        self.description = ""
        self.request: Optional[Request] = None
        self.tags = tags
        self.parameters: List[Parameter] = []
        self.responses: List[Response] = []

        for status_code, media_type in responses.items():
            self.responses.append(Response(media_type, status_code))

    def __call__(self, target: T) -> T:

        annotations = target.__annotations__
        docstring = DocString(target)

        self.summary = docstring.short_description
        self.description = docstring.long_description

        # Build params doc list
        params_doc = {}
        for param in docstring.find_component_by_type("param", "parameter"):
            params_doc[param.attributes[-1]] = param

        for name, value in annotations.items():
            if name == "return":
                self.responses.append(Response(value, 200))
                continue
            if isinstance(value, Parameter):
                value.name = name
                if name in params_doc:
                    value.description = params_doc[name].description
                self.parameters.append(value)
            elif isinstance(value, Schema):
                raise ValueError(
                    "Schema object has to be packed in corresponding media type."
                )
            elif isinstance(value, MediaType):
                self.request = Request(
                    value,
                    params_doc[name].description if name in params_doc else "",
                    True,
                )
            else:
                raise ValueError(
                    f"Parameter {name} has unsupported type or unknown localisation."
                )
        self._parse_responses_description(docstring)
        bind_annotation(target, self)
        Api.register(self)
        return target

    def _parse_responses_description(self, docstring: DocString) -> None:

        for response_doc in docstring.find_component_by_type("return", "returns"):
            response_code = 200
            if response_doc.attributes:
                response_code = int(response_doc.attributes[-1])

            for response in self.responses:
                if response.status_code == response_code:
                    response.description = response_doc.description

    def to_doc(self) -> dict:
        doc: Dict[Union[str, int], Any] = {
            "description": self.description,
            "summary": self.summary,
        }

        if self.parameters:
            doc["parameters"] = []
            for parameter in self.parameters:
                doc["parameters"].append(parameter.to_doc())

        if self.tags:
            doc["tags"] = self.tags

        doc["responses"] = {}
        for response in self.responses:
            doc["responses"][str(response.status_code)] = response.to_doc()

        if self.request:
            doc["requestBody"] = self.request.to_doc()

        return doc


__all__ = ["Operation"]
