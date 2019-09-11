from typing import Any
from typing import Callable
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

    def __call__(self, target: T) -> T:
        schema = Object(
            title=self.title,
            description=self.description,
            required=self.required,
            deprecated=self.deprecated,
            properties=target.__dict__["__annotations__"],
        )
        mappings: Dict[str, Union[str, Callable]] = self.mapping

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

        def _create_from(obj: object) -> T:

            if isinstance(obj, dict):
                return resource(**obj)

            object_type: str = type(obj)
            if object_type not in mappings:
                raise ValueError(
                    f"Object of type {object_type} could not be mapped to ValueObject. "
                    f"Have you forgot to define mapping for the object?"
                )
            mapping = mappings[object_type]
            result: Dict[str, Any] = {}
            for key, attribute in schema.properties.items():
                if key not in mapping:
                    if attribute.nullable:
                        result[key] = None
                    else:
                        raise ValueError(
                            f"Property `{key}` is not nullable, "
                            f"and must be defined in mapping scheme for {obj.__class__}"
                        )
                    continue

                mapped_key = mapping[key]
                if isinstance(mapped_key, str):
                    result[key] = getattr(obj, mapped_key)
                elif mapped_key is True or mapped_key == 1:
                    result[key] = getattr(obj, key)
                elif isinstance(mapped_key, Callable):
                    result[key] = mapped_key(obj)
                else:
                    raise ValueError(
                        f"Property {key} has invalid mapping setting for object {obj.__class__}."
                    )

            return resource(**result)

        resource.create_from = _create_from
        OpenApi.add_resource(resource, self)

        return resource


__all__ = ["Resource"]
