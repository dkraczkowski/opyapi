from __future__ import annotations
from ..exceptions import ValidationError
from .validator import Validator


class Truthy(Validator):
    def validate(self, value):
        if isinstance(value, str):
            value = value.lower()
        if value not in (1, "1", True, "ok", "yes", "true"):
            raise ValidationError(
                f"Passed value {value} is not valid truthy expression."
            )
        return True
