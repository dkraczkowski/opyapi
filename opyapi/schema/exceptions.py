from __future__ import annotations


class ValidationError(ValueError):
    def __bool__(self):
        return False
