import numbers
from typing import Any
from typing import Optional

from .type import Type
from opyapi.schema.validators import validate_multiple_of
from opyapi.schema.validators import validate_range


class Number(Type):

    accept_types = numbers.Number
    reject_types = bool
    type = "number"

    def __init__(
        self,
        minimum: Optional[float] = None,
        maximum: Optional[float] = None,
        multiple_of: Optional[float] = None,
        nullable: bool = False,
        default: Optional[float] = None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        self.minimum = minimum
        self.maximum = maximum
        self.multiple_of = multiple_of
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated
        self.read_only = read_only
        self.write_only = write_only

    def validate(self, value: Any):
        super().validate(value)

        if self.minimum is not None or self.maximum is not None:
            validate_range(value, self.minimum, self.maximum)

        if self.multiple_of is not None:
            validate_multiple_of(value, self.multiple_of)


__all__ = ["Number"]
