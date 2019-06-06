import re

from ..exceptions import ValidationError
from .validator import Validator

_UUID_REGEX = re.compile(
    r"^(?:urn:uuid:)?[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$", re.I
)


class Uuid(Validator):
    def validate(self, value: str) -> str:

        if not _UUID_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid uuid.")
        return value
