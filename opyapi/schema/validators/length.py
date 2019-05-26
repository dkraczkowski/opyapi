from __future__ import annotations

from .validator import Validator
from ..exceptions import InvalidLengthError


class Length(Validator):
    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value):
        if self.minimum is not None and len(value) < self.minimum:
            raise InvalidLengthError(
                f"Passed value `{value}` is shorter than set minimum length `{self.minimum}`."
            )

        if self.maximum is not None and len(value) > self.maximum:
            raise InvalidLengthError(
                f"Passed value `{value}` is longer than set maximum length `{self.maximum}`."
            )

        return value
