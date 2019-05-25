from __future__ import annotations
from abc import ABC, abstractmethod
from ..exceptions import ValidationError


class Validator(ABC):

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError

    def is_valid(self, value) -> bool:
        try:
            self.validate(value)
            return True
        except ValidationError:
            return False
