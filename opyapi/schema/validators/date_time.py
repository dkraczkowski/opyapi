from datetime import datetime
import re

from .validator import Validator
from ..exceptions import ValidationError

_ISO_8601_DATETIME_REGEX = re.compile(
    r"^(\d{4})-?([0-1]\d)-?([0-3]\d)[t\s]?([0-2]\d:?[0-5]\d:?[0-5]\d|23:59:60|235960)(\.\d+)?(z|[+-]\d{2}:\d{2})$",
    re.I,
)


class DateTime(Validator):
    """
    :: _ISO Standard: http://tools.ietf.org/html/rfc3339#section-5.6
    """

    def validate(self, value: str) -> datetime:
        if not _ISO_8601_DATETIME_REGEX.match(value):
            raise ValidationError(
                f"Passed value {value} is not valid ISO 8601 date time."
            )
        parts = _ISO_8601_DATETIME_REGEX.findall(value)[0]
        time = parts[3]
        if ":" in time:
            time = time.split(":")
        else:
            time = list(map("".join, zip(*[iter(time)] * 2)))
        return datetime(
            year=int(parts[0]),
            month=int(parts[1]),
            day=int(parts[2]),
            hour=int(time[0]),
            minute=int(time[1]),
            second=int(time[2]),
        )
