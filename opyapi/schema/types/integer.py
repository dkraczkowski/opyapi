from __future__ import annotations

from .type import Type
from ..schema import Schema


class Integer(Type, Schema):

    type = "integer"
    accept_types = int
    reject_types = bool
    minimum: int = None
    maximum: int = None
    multiple_of: int = None

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
        self.minimum = minimum
        self.maximum = maximum
        self.multiple_of = multiple_of
        self.description = description
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated

    def to_doc(self):
        doc = self._get_base_doc()

        if self.minimum is not None:
            doc["minimum"] = self.minimum

        if self.maximum is not None:
            doc["maximum"] = self.maximum

        if self.multiple_of is not None:
            doc["multipleOf"] = self.multiple_of

        return doc

    def validate(self, value):
        if self.minimum is not None or self.maximum is not None:

        super().validate(value)
