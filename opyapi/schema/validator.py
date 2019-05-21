from __future__ import annotations
from typing import Callable
from .exceptions import ValidationError


def validator(target):
    """
    Decorator that makes given function a validator.

    Example::
    @validator
    def isinteger(value):
        return isinstance(value, int)

    :return function:
    """

    def wrapper(func: Callable, *args, **kwargs):
        passed = func(*args, **kwargs)
        if not passed:
            return ValidationError(func, *args, **kwargs)
        return True

    return wrapper
