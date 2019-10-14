from typing import Any
from typing import List
from typing import Optional
from typing import Union

from .type import Type
from opyapi.schema.errors import ValidationError


class Enum(Type):
    accept_types = (str, int, float)
    type = "string"

    def __init__(
        self,
        *args: List[str],
        nullable: bool = False,
        default: Optional[Union[str, int, float]] = None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        super().__init__()
        self.allowed_values = args
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
        self.nullable = nullable

    def validate(self, value: Any) -> None:
        super().validate(value)

        if value not in self.allowed_values:
            raise ValidationError(
                f"Passed value `{value}` is not within allowed values `{self.allowed_values}`."
            )

        return value


__all__ = ["Enum"]
