from __future__ import annotations
from ..exceptions import ValidationError
from .validator import Validator


class Falsy(Validator):
    def validate(self, value):
        if isinstance(value, str):
            value = value.lower()
        if value not in (0, "0", False, "no", "nope", "false"):
            raise ValidationError(f"Passed value {value} is not valid falsy expression.")
        return False
