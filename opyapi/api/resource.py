from typing import Any
from typing import Dict
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from . import Annotation
from ..exceptions import ValidationError
from ..schema.types import Object
from ..schema.types import Type as SchemaType
from .openapi import OpenApi

T = TypeVar("T")


class Resource(Annotation):
    """
    Resource replaces Open Api Schema Objects to simplify documentation process.

    .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """

    def __init__(
        self,
        title: str,
        description: str = "",
        id: str = "",
        required: Union[tuple, list] = (),
        deprecated: bool = False,
        mapping: Optional[Dict[str, Any]] = None,
    ):
        self.id = id
        self.mapping = mapping
        self.title = title
        self.description = description
        self.required = required
        self.deprecated = deprecated

    def __call__(self, target: Type[T]) -> T:
        schema = Object(
            title=self.title,
            description=self.description,
            required=self.required,
            deprecated=self.deprecated,
            properties=target.__dict__["__annotations__"],
        )

        def _init(instance, **kwargs) -> None:
            super(target, instance).__setattr__("_data", {})  # skip _setattr
            for key, value in kwargs.items():
                instance.__setattr__(key, value)

        def _getattr(instance, attribute_name):
            if attribute_name not in schema.properties:
                raise ValidationError(
                    f"Attribute `{attribute_name}` is not specified for resource {target}."
                )

            return (
                instance._data[attribute_name]
                if attribute_name in instance._data
                else None
            )

        def _setattr(instance, attribute_name, value) -> None:
            if attribute_name not in schema.properties:
                raise ValidationError(
                    f"Attribute `{attribute_name}` is not specified for resource {target}."
                )
            schema.properties[attribute_name].validate(value)
            instance._data[attribute_name] = value

        def _to_doc() -> dict:
            return schema.to_doc()

        def _to_dict(instance) -> dict:
            result = {}
            for key, value in instance._data.items():
                if schema[key].write_only:
                    continue
                result[key] = value

            return result

        resource = type(
            target.__name__ + "Resource",
            (target, SchemaType),
            {
                "__init__": _init,
                "__getattr__": _getattr,
                "__setattr__": _setattr,
                "to_dict": _to_dict,
                "to_doc": _to_doc,
            },
        )
        OpenApi.add_resource(resource, self)

        return resource


__all__ = ["Resource"]
