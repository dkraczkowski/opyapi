from __future__ import annotations

from .validator import Validator
from ..exceptions import NotInRangeError


class Range(Validator):

    minimum = None
    maximum = None

    def __init__(self, minimum=None, maximum=None):
        if minimum:
            self.minimum = minimum

        if maximum:
            self.maximum = maximum

    def validate(self, value):
        if self.minimum and value < self.minimum:
            raise NotInRangeError(
                f"Passed value `{value}` is lower than set minimum value `{self.minimum}`."
            )

        if self.maximum and value > self.maximum:
            raise NotInRangeError(
                f"Passed value `{value}` is greater than set maximum value `{self.maximum}`."
            )

        return True
