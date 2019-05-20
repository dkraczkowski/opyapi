from __future__ import annotations
from typing import Callable


class ValidationError(ValueError):
    def __init__(self, validator: Callable, args: list, kwargs: dict):
        self.validator = validator
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return "ValidationError(validator={validator}, args={args}, kwargs={kwargs})".format(
            validator=self.validator.__name__, args=self.args, kwargs=self.kwargs
        )

    def __bool__(self):
        return False
