from typing import Optional
from typing import Union

from ...exceptions import InvalidLengthError
from .validator import Validator


class Capacity(Validator):

    minimum_items: Optional[int] = None
    maximum_items: Optional[int] = None
    name: str = "capacity"

    def __init__(self, minimum: Optional[int] = None, maximum: Optional[int] = None):
        if minimum:
            self.minimum_items = minimum

        if maximum:
            self.maximum_items = maximum

    def validate(self, value: Union[list, tuple]) -> Union[list, tuple]:
        length = len(value)

        if self.minimum_items is not None and length < self.minimum_items:
            raise InvalidLengthError(
                f"Passed collection cannot be empty and must contain at least `{self.minimum_items}` items."
            )

        if self.maximum_items is not None and length > self.maximum_items:
            raise InvalidLengthError(
                f"Passed collection cannot contain more than `{self.maximum_items}` items."
            )

        return value


__all__ = ["Capacity"]
