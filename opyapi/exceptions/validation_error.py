from .http_error import HttpError


class ValidationError(HttpError, ValueError):
    status_code: int = 400
    http_body = "Input validation error"

    def __bool__(self):
        return False


class InvalidRangeError(ValidationError):
    pass


class InvalidLengthError(ValidationError):
    pass


__all__ = ["ValidationError", "InvalidRangeError", "InvalidLengthError"]
