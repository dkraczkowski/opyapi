from typing import Any
from typing import Dict
from typing import Optional
from typing import Type as BaseType
from typing import TypeVar
from typing import Union

from .annotation import Annotation
from .annotation import bind_annotation
from .api import Api
from opyapi.schema import Schema as BaseSchema
from opyapi.schema.types import Array
from opyapi.schema.types import Enum
from opyapi.schema.types import Integer
from opyapi.schema.types import Number
from opyapi.schema.types import Object
from opyapi.schema.types import String
from opyapi.schema.types import Type

T = TypeVar("T")


class Schema(Annotation):
    """
        Schema replaces Open Api Schema Objects to simplify documentation process.

        .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """

    def __init__(
        self,
        title: str = "",
        description: str = "",
        id: str = "",
        required: Union[tuple, list] = (),
        deprecated: bool = False,
        mapping: Optional[Dict[Type, Dict]] = None,
    ):
        self.id = id
        self.mapping = mapping
        self.title = title
        self.description = description
        self.required = required
        self.deprecated = deprecated

    def __call__(self, target: Any) -> BaseType[BaseSchema]:
        schema_definition = Object(
            title=self.title,
            description=self.description,
            required=self.required,
            deprecated=self.deprecated,
            properties=target.__dict__["__annotations__"],
        )
        mappings = self.mapping

        SchemaType = type(
            target.__name__ + "Schema",
            (target, BaseSchema),
            {
                "__name__": target.__name__,
                "__mappings__": mappings,
                "__schema__": schema_definition,
            },
        )

        bind_annotation(SchemaType, self)
        Api.register(self)

        return SchemaType


def generate_doc_from_schema(obj: Any) -> dict:
    if hasattr(obj, "__schema__"):
        obj = obj.__schema__
    elif not isinstance(obj, Type):
        obj = Type.from_basic_type(obj)

    result: Dict[str, Any] = {"type": obj.type}

    if obj.nullable:
        result["nullable"] = obj.nullable

    if obj.default is not None:
        result["default"] = obj.default

    if obj.deprecated:
        result["deprecated"] = obj.deprecated

    if obj.description:
        result["description"] = obj.description

    if obj.read_only:
        result["readOnly"] = obj.read_only

    if obj.write_only:
        result["writeOnly"] = obj.write_only

    if isinstance(obj, Array):
        if obj.items:
            result["items"] = generate_doc_from_schema(obj.items)
        if obj.min_length:
            result["minItems"] = obj.min_length
        if obj.max_length:
            result["maxItems"] = obj.max_length
        if obj.unique_items:
            result["uniqueItems"] = obj.unique_items

    if isinstance(obj, Enum):
        result["enum"] = obj.allowed_values

    if isinstance(obj, (Number, Integer)):
        if obj.minimum is not None:
            result["minimum"] = obj.minimum

        if obj.maximum is not None:
            result["maximum"] = obj.maximum

        if obj.multiple_of is not None:
            result["multipleOf"] = obj.multiple_of

    if isinstance(obj, Object):
        if obj.required:
            result["required"] = obj.required

        result["properties"] = {}
        for key, prop in obj.properties.items():
            result["properties"][key] = generate_doc_from_schema(prop)

    if isinstance(obj, String):
        if obj.min_length is not None:
            result["minLength"] = obj.min_length

        if obj.max_length is not None:
            result["maxLength"] = obj.max_length

        if obj.pattern is not None:
            result["pattern"] = obj.pattern

        if obj.format is not None:
            result["format"] = str(obj.format)

    return result


__all__ = ["Schema", "generate_doc_from_schema"]
