from __future__ import annotations

from .validator import Validator
from ..exceptions import ValidationError


class Capacity(Validator):

    minimum_items: int = None
    maximum_items: int = None
    name: str = "capacity"

    def __init__(self, minimum=None, maximum=None):
        if minimum:
            self.minimum_items = minimum

        if maximum:
            self.maximum_items = maximum

    def validate(self, value):
        length = len(value)

        if self.minimum_items and length < self.minimum_items:
            raise ValidationError(
                f"Passed collection cannot be empty and must contain at least `{self.minimum_items}` items."
            )

        if self.maximum_items and length < self.maximum_items:
            raise ValidationError(
                f"Passed collection cannot contain more than `{self.maximum_items}` items."
            )
