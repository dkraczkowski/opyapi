from . import ValidationError


def validator(target, *args, **kwargs):
    """
    Decorator that makes given function a validator.

    Example::
    @validator
    def isinteger(value):
        return isinstance(value, int)

    :return function:
    """

    def wrapper(func: function, *args, **kwargs):
        passed = func(*args, **kwargs)
        if not passed:
            return ValidationError(func, *args, **kwargs)
        return True

    return wrapper(target, *args, **kwargs)
