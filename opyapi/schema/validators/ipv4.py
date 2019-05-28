from __future__ import annotations
import re
from ..exceptions import ValidationError
from .validator import Validator

_IPV4_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$",
    re.I
)


class Ipv4(Validator):
    def validate(self, value):

        if not _IPV4_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid ipv4 address.")
        return value
