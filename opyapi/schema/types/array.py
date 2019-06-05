from __future__ import annotations

from .type import Type
from ..validators import Capacity
from ..exceptions import ValidationError


class Array(Type):

    accept_types = (tuple, list)
    type = "array"

    def __init__(
        self,
        items: Type = None,
        min_length: int = None,
        max_length: int = None,
        unique_items: bool = None,
        description: str = "",
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = None,
        write_only: bool = None,
    ):
        super().__init__()
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
        self.nullable = nullable
        self.description = description
        self.unique_items = unique_items
        self.max_length = max_length
        self.min_length = min_length
        self.items_type = items

        if self.min_length is not None or self.max_length is not None:
            self.extra_validators.append(
                Capacity(minimum=self.min_length, maximum=self.max_length)
            )

    def validate(self, value):
        super().validate(value)

        if self.unique_items and not len(set(value)) == len(value):
            raise ValidationError(
                "Items in the array should be unique, passed array contains duplicates."
            )

        if isinstance(self.items_type, Type):
            for item in value:
                self.items_type.validate(item)
        return value

    def to_doc(self):
        doc = self._get_base_doc()
        if self.items_type:
            doc["items"] = self.items_type.to_doc()
        if self.min_length:
            doc["minItems"] = self.min_length
        if self.max_length:
            doc["maxItems"] = self.max_length
        if self.unique_items:
            doc["uniqueItems"] = self.unique_items
