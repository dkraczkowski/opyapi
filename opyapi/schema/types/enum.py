from __future__ import annotations

from .type import Type
from ..exceptions import ValidationError


class Enum(Type):

    accept_types = (str, int, float)
    type = "string"

    def __init__(
        self,
        *args,
        description: str = "",
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = None,
        write_only: bool = None,
    ):
        super().__init__()
        self.allowed_values = args
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
        self.nullable = nullable
        self.description = description

    def validate(self, value):
        super().validate(value)

        if value not in self.allowed_values:
            raise ValidationError(
                f"Passed value `{value}` is not within allowed values `{self.allowed_values}`."
            )

        return value

    def to_doc(self):
        doc = self._get_base_doc()
        doc["enum"] = self.allowed_values

        return doc
