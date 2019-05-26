from __future__ import annotations

from .validator import Validator


class Pattern(Validator):

    def __init__(self, pattern):
        self.pattern = pattern

    def validate(self, value):

        return value
