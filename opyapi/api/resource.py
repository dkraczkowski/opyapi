from typing import Type, TypeVar, Optional

from . import Annotation
from ..application import Application
from ..schema import Object
from ..schema.types import Type as SchemaType

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
        required: tuple = (),
        deprecated: bool = False,
        mapping: Optional[dict] = None,
    ) -> None:
        self._attributes = {
            "title": title,
            "description": description,
            "required": required,
            "deprecated": deprecated,
            "mapping": mapping,
        }

    def __call__(self, target: Type[T]) -> T:
        schema = Object(
            properties=target.__dict__["__annotations__"],
            title=self._attributes["title"],
            description=self._attributes["description"],
            required=self._attributes["required"],
            deprecated=self._attributes["deprecated"],
        )
        target._data = {}

        def _init(instance, **kwargs):
            kwargs = schema.validate(kwargs)
            super(target, instance).__setattr__("_data", {})
            for key, value in kwargs.items():
                instance.__setattr__(key, value)

        def _getattr(instance, name):
            if name not in instance.schema.properties:
                raise AttributeError(
                    f"Attribute `{name}` is not specified for resource {target}."
                )

            return instance._data[name] if name in instance._data else None

        def _setattr(instance, name, value):

            if name not in instance.schema.properties:
                raise AttributeError(
                    f"Attribute `{name}` is not specified for resource {target}."
                )

            instance._data[name] = value

        def _to_dict(instance) -> dict:
            result = {}
            for key, value in instance._data.items():
                if schema[key].write_only:
                    continue
                result[key] = value

            return result

        resource = type(
            target.__name__ + "Resource",
            (target, Resource, SchemaType),
            {
                "schema": schema,
                "_data": {},
                "__init__": _init,
                "__getattr__": _getattr,
                "__setattr__": _setattr,
                "to_dict": _to_dict,
            },
        )
        Application.add_resource(resource)

        return resource
