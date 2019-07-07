import re

from .validator import Validator
from opyapi.exceptions import ValidationError

_IPV4_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$", re.I
)


class Ipv4(Validator):
    def validate(self, value: str) -> str:

        if not _IPV4_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid ipv4 address.")

        return value


__all__ = ["Ipv4"]
