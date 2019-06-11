import re

from .validator import Validator
from ..exceptions import ValidationError

_URI_REGEX = re.compile(r"^(?:[a-z][a-z0-9+-.]*:)(?:\\/?\\/)?[^\s]*$", re.I)


class Uri(Validator):
    def validate(self, value: str) -> str:

        if not _URI_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid uri.")
        return value
