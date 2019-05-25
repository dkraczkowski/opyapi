from __future__ import annotations

from ..validators import Validator
from ..exceptions import ValidationError


class Type(Validator):
    """
    Reflects available types in the open annotations specification

    :: _Open Api types: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#data-types
    """

    accept_types = ()
    reject_types = ()
    type: str = None

    def validate(self, value):
        if not isinstance(value, self.accept_types) or isinstance(value, self.reject_types):
            raise ValidationError(
                f"Could not validate passed value `{value}` as a valid {self.type}."
            )
        return value
