from typing import Union

from ..exceptions import ValidationError
from .validator import Validator


class Falsy(Validator):
    def validate(self, value: Union[bool, int, str]) -> bool:
        if isinstance(value, str):
            value = value.lower()
        if value not in (0, "0", False, "no", "nope", "false"):
            raise ValidationError(
                f"Passed value {value} is not valid falsy expression."
            )
        return False
