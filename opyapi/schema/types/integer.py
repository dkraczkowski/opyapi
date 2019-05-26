from __future__ import annotations

from .type import Type
from ..validators import Range
from ..validators import MultipleOf


class Integer(Type):

    type = "integer"
    accept_types = int
    reject_types = bool

    def __init__(
        self,
        minimum: int = None,
        maximum: int = None,
        multiple_of: int = None,
        description: str = "",
        nullable: bool = False,
        default=None,
        deprecated: bool = False
    ):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum
        self.multiple_of = multiple_of
        self.description = description
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated

        if self.minimum is not None or self.maximum is not None:
            self.extra_validators.append(Range(minimum=self.minimum, maximum=self.maximum))

        if self.multiple_of is not None:
            self.extra_validators.append(MultipleOf(self.multiple_of))

    def to_doc(self):
        doc = self._get_base_doc()

        if self.minimum is not None:
            doc["minimum"] = self.minimum

        if self.maximum is not None:
            doc["maximum"] = self.maximum

        if self.multiple_of is not None:
            doc["multipleOf"] = self.multiple_of

        return doc

