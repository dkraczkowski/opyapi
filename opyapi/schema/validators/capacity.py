from typing import Union

from .validator import Validator
from ..exceptions import InvalidLengthError


class Capacity(Validator):

    minimum_items: int = None
    maximum_items: int = None
    name: str = "capacity"

    def __init__(self, minimum=None, maximum=None):
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
