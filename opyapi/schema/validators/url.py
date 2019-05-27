from __future__ import annotations
import re
from ..exceptions import ValidationError
from .validator import Validator

_URL_REGEX = re.compile(
    r".*",
    re.I | re.U,
)


class Url(Validator):
    def validate(self, value):

        if not _URL_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid url.")
        return value
