from datetime import date
import re

from .validator import Validator
from ..exceptions import ValidationError

_ISO_8601_DATE_REGEX = re.compile(r"^(\d{4})-?([0-1]\d)-?([0-3]\d)$", re.I)


class Date(Validator):
    """
    :: _ISO Standard: https://tools.ietf.org/html/rfc3339#section-5.6
    """

    def validate(self, value: str) -> date:
        if not _ISO_8601_DATE_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid ISO 8601 date.")
        parts = _ISO_8601_DATE_REGEX.findall(value)[0]

        return date(year=int(parts[0]), month=int(parts[1]), day=int(parts[2]))
