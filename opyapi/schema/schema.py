from abc import ABCMeta
from typing import Any
from typing import Dict
from typing import Type
from typing import List
from .validators.validate import validate
from .errors import ValidationError
from .types import Object
from .types import String


class SchemaMeta(ABCMeta):
    def __new__(mcs: "SchemaMeta", name: str, bases: tuple, namespace: dict, **kwargs):
        if (
            f"{namespace['__module__']}.{namespace['__qualname__']}"
            == "opyapi.schema.schema.Schema"
        ):
            return super().__new__(mcs, name, bases, namespace)

        klass = super().__new__(mcs, name, bases, namespace)
        required = []
        if "required" in kwargs:
            required = kwargs["required"]
        schema_definition = Object(properties=klass.__annotations__, required=required)
        klass.__schema__ = schema_definition

        return klass


class Schema(metaclass=SchemaMeta):
    __data__: Dict[str, Any]
    __schema__: Object
    __mappings__: Dict[Type, Dict]

    def __init__(self, **kwargs) -> None:
        super().__setattr__('__data__', {})
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __getattr__(self, attribute_name):
        if attribute_name not in self.__schema__.properties:
            raise AttributeError(
                f"Attribute `{attribute_name}` is not specified in {self}."
            )

        return (
            self.__data__[attribute_name] if attribute_name in self.__data__ else None
        )

    def __setattr__(self, attribute_name: str, value: Any) -> None:
        if attribute_name not in self.__schema__.properties:
            raise AttributeError(
                f"Attribute `{attribute_name}` is not specified in {self}."
            )
        property_meta = self.__schema__.properties[attribute_name]
        if isinstance(property_meta, String):
            try:
                value = property_meta.format_value(value)
            except ValueError as e:
                raise ValidationError(str(e))
        else:
            validate(value, property_meta)

        self.__data__[attribute_name] = value

    def to_dict(self) -> dict:
        result = {}
        for key, value in self.__data__.items():
            if self.__schema__[key].write_only:
                continue
            result[key] = value

        return result

    @classmethod
    def create_from(cls, obj: object) -> "Schema":
        if isinstance(obj, dict):
            return cls(**obj)

        object_type: Type = type(obj)
        if object_type not in cls.__mappings__:
            raise ValueError(
                f"Object of type {object_type} could not be mapped to {cls.__name__}. "
                f"Have you forgot to define mapping for the object?"
            )
        mapping = cls.__mappings__[object_type]
        result: Dict[str, Any] = {}
        for key, attribute in cls.__schema__.properties.items():
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
            elif callable(mapped_key):
                result[key] = mapped_key(obj)
            else:
                raise ValueError(
                    f"Property {key} has invalid mapping setting for object {obj.__class__}."
                )

        return cls(**result)


__all__ = ["Schema"]
