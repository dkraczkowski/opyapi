from typing import Any
from typing import Optional

from opyapi.schema.validators import validate_multiple_of
from opyapi.schema.validators import validate_range
from .type import Type


class Integer(Type):

    type = "integer"
    accept_types = int
    reject_types = bool

    def __init__(
        self,
        minimum: Optional[int] = None,
        maximum: Optional[int] = None,
        multiple_of: Optional[int] = None,
        nullable: bool = False,
        default: Optional[int] = None,
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


__all__ = ["Integer"]
