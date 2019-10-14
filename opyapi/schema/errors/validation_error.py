from opyapi import OpyapiError


class ValidationError(OpyapiError, ValueError):
    def __bool__(self):
        return False


__all__ = ["ValidationError"]
