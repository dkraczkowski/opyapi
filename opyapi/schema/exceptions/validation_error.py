from __future__ import annotations


class ValidationError(ValueError):
    def __bool__(self):
        return False


class InvalidRangeError(ValidationError):
    pass


class InvalidLengthError(ValidationError):
    pass
