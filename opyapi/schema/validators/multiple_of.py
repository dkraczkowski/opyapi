from typing import Union

from .validator import Validator
from ..exceptions import ValidationError


class MultipleOf(Validator):
    def __init__(self, multiple_of: Union[int, float]):
        self.multiple_of = multiple_of

    def validate(self, value: Union[int, float]) -> Union[int, float]:
        if not value % self.multiple_of == 0:
            raise ValidationError(
                f"Passed value `{value}` must be multiplication of {self.multiple_of}."
            )

        return value
