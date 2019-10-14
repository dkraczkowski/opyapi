from typing import Optional
from typing import Union

from opyapi.schema.errors import ValidationError
from opyapi.schema import validators
from .type import Type


class Array(Type):
    accept_types = (tuple, list, set)
    type = "array"

    def __init__(
        self,
        items: Optional[Type] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        unique_items: bool = False,
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
        self.nullable = nullable
        self.unique_items = unique_items
        self.max_length = max_length
        self.min_length = min_length
        self._items = None
        self.items = items

    @property
    def items(self) -> Optional[Type]:
        return self._items

    @items.setter
    def items(self, value: Type) -> None:
        """
        #todo: https://json-schema.org/understanding-json-schema/reference/array.html#tuple-validation tuple support
        :param Type value:
        :return:
        """
        if value and not isinstance(value, Type):
            raise ValueError(
                "items argument must be either None or instance of opyapi.schema.Type"
            )
        self._items = value

    def validate(self, value: Union[list, tuple]) -> None:
        super().validate(value)

        if self.unique_items and not len(set(value)) == len(value):
            raise ValidationError(
                "Items in the array should be unique, passed array contains duplicates."
            )

        if isinstance(self.items, Type):
            for item in value:
                self.items.validate(item)

        if self.min_length or self.max_length:
            validators.validate_length(value, self.min_length, self.max_length)


__all__ = ["Array"]
