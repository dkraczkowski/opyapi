from __future__ import annotations
from ..exceptions import ValidationError


class Validator:
    def validate(self, value):
        raise NotImplementedError

    def is_valid(self, value) -> bool:
        try:
            self.validate(value)
            return True
        except ValidationError:
            return False
