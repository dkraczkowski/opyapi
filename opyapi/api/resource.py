from __future__ import annotations
from . import Annotation
from ..schema.types import Type
from ..schema import Object


class Resource(Annotation):
    """
    Resource replaces Open Api Schema Objects to simplify documentation process.

    .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """

    def __init__(
        self,
        title: str,
        description: str = "",
        required: tuple = None,
        deprecated: bool = False,
    ):
        self._attributes = {
            "title": title,
            "description": description,
            "required": required,
            "deprecated": deprecated,
        }

    def __call__(self, target):
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

        return type(
            target.__name__ + "Resource",
            (target, Resource, Type),
            {
                "schema": schema,
                "_data": {},
                "__init__": _init,
                "__getattr__": _getattr,
                "__setattr__": _setattr,
            },
        )
