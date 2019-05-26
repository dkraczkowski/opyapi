from __future__ import annotations
from datetime import time
import re

from .validator import Validator
from ..exceptions import ValidationError

_ISO_8601_TIME_REGEX = re.compile(
    r"^(?P<time>[0-2]\d:?[0-5]\d:?[0-5]\d|23:59:60|235960)(?P<microseconds>\.\d+)?(?P<tzpart>z|[+-]\d{2}:\d{2})?$",
    re.I,
)


class Time(Validator):
    """
    :: _ISO Standard: http://tools.ietf.org/html/rfc3339#section-5.6
    """

    def validate(self, value):
        if not _ISO_8601_TIME_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid ISO 8601 time.")
        parts = _ISO_8601_TIME_REGEX.fullmatch(value)
        time_parts = parts.group("time")
        if ":" in time_parts:
            time_parts = time_parts.split(":")
        else:
            time_parts = list(map("".join, zip(*[iter(time_parts)] * 2)))

        microseconds = parts.group("microseconds")
        if microseconds is not None:
            microseconds = int(microseconds[1:])
        else:
            microseconds = 0

        return time(
            hour=int(time_parts[0]),
            minute=int(time_parts[1]),
            second=int(time_parts[2]),
            microsecond=microseconds,
        )
