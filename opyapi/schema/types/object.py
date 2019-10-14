from typing import Union

from .type import Type
from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate


class Object(Type):

    accept_types = (object, dict)
    type = "object"

    def __init__(
        self,
        properties: dict = {},
        required: Union[list, tuple] = (),
        nullable: bool = False,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.nullable = nullable
        self.properties = properties
        self.required = required if required is not None else ()

    def __getitem__(self, key: str) -> Type:
        return self.properties[key]

    def __setitem__(self, key: str, value: Type):
        self.properties[key] = value

    def validate(self, value: dict) -> None:
        super().validate(value)
        for prop in self.required:
            if prop not in value:
                raise ValidationError(
                    f"Missing required property `{prop}` in passed dataset `{value}`"
                )

        for key, prop in self.properties.items():
            if key not in value:
                continue
            validate(value[key], prop)


__all__ = ["Object"]
