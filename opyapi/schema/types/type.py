from typing import Any
from typing import Type as BaseType
from typing import Union

from opyapi.schema.errors import ValidationError


class Type:
    """
    Reflects available types in the open api specification

    :: _Open Api types: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#data-types
    """

    type: str = ""
    default: Any = None
    read_only: bool = False
    write_only: bool = False
    nullable: bool
    deprecated: bool = False
    accept_types: Union[tuple, BaseType] = ()
    reject_types: Union[tuple, BaseType] = ()

    def validate(self, value: Any) -> None:
        if value is None and self.nullable:
            return

        if not isinstance(value, self.accept_types) or isinstance(
            value, self.reject_types
        ):
            raise ValidationError(
                f"Could not validate passed value `{value}` as a valid {self.type}."
            )

    @classmethod
    def from_basic_type(cls, basic_type: BaseType) -> "Type":
        if basic_type is int:
            from .integer import Integer

            return Integer()

        if basic_type is bool:
            from .boolean import Boolean

            return Boolean()

        if basic_type is float:
            from .number import Number

            return Number()

        if basic_type is str:
            from .string import String

            return String()

        if basic_type is list:
            from .array import Array

            return Array()

        raise ValueError(f"Cannot generate schema from passed type {basic_type}.")


__all__ = ["Type"]
