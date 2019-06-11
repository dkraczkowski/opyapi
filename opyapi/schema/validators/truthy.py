from .validator import Validator
from ..exceptions import ValidationError


class Truthy(Validator):
    def validate(self, value: str) -> bool:
        if isinstance(value, str):
            value = value.lower()
        if value not in (1, "1", True, "ok", "yes", "true"):
            raise ValidationError(
                f"Passed value {value} is not valid truthy expression."
            )
        return True
