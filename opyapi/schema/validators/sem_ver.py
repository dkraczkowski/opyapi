import re

from .validator import Validator
from opyapi.exceptions import ValidationError

_SEMVER_REGEX = re.compile(
    r"^((([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9a-z-]+(?:\.[0-9a-z-]+)*))?)(?:\+([0-9a-z-]+(?:\.[0-9a-z-]+)*))?)$",
    re.I,
)


class SemVer(Validator):
    def validate(self, value: str) -> str:

        if not _SEMVER_REGEX.match(value):
            raise ValidationError(
                f"Passed value {value} is not valid semantic version number."
            )
        return value


__all__ = ["SemVer"]
