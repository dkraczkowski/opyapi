from __future__ import annotations

from .type import Type


class String(Type):

    accept_types = str
    reject_types = bool
    type = "string"

    def __init__(
        self,
        format: str = None,
        min_length: int = None,
        max_length: int = None,
        pattern: str = None
    ):
        super().__init__()
        if format is not None:
            self.format = format

        if min_length is not None:
            self.min_length = min_length

        if max_length is not None:
            self.max_length = max_length

        if pattern is not None:
            self.pattern = pattern
