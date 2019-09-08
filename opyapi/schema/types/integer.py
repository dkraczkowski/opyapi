from typing import Optional

from ..validators import MultipleOf
from ..validators import Range
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
        description: str = "",
        nullable: bool = False,
        default: Optional[int] = None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum
        self.multiple_of = multiple_of
        self.description = description
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated
        self.read_only = read_only
        self.write_only = write_only

        if self.minimum is not None or self.maximum is not None:
            self.extra_validators.append(
                Range(minimum=self.minimum, maximum=self.maximum)
            )

        if self.multiple_of is not None:
            self.extra_validators.append(MultipleOf(self.multiple_of))

    def to_doc(self) -> dict:
        doc = super().to_doc()

        if self.minimum is not None:
            doc["minimum"] = self.minimum

        if self.maximum is not None:
            doc["maximum"] = self.maximum

        if self.multiple_of is not None:
            doc["multipleOf"] = self.multiple_of

        return doc


__all__ = ["Integer"]
