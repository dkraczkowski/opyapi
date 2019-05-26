from __future__ import annotations

from .validator import Validator
from ..exceptions import NotInRangeError


class Range(Validator):

    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value):
        if self.minimum is not None and value < self.minimum:
            raise NotInRangeError(
                f"Passed value `{value}` is lower than set minimum value `{self.minimum}`."
            )

        if self.maximum is not None and value > self.maximum:
            raise NotInRangeError(
                f"Passed value `{value}` is greater than set maximum value `{self.maximum}`."
            )

        return value
