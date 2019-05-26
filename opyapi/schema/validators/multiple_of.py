from __future__ import annotations

from .validator import Validator
from ..exceptions import ValidationError


class MultipleOf(Validator):
    def __init__(self, multiple_of):
        self.multiple_of = multiple_of

    def validate(self, value):
        if not value % self.multiple_of == 0:
            raise ValidationError(
                f"Passed value `{value}` must be multiplication of {self.multiple_of}."
            )

        return value
