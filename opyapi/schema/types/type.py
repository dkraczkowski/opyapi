from __future__ import annotations
from ..validators import Validator
from ..exceptions import ValidationError
from ..schema import Schema


class Type(Validator, Schema):
    """
    Reflects available types in the open api specification

    :: _Open Api types: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#data-types
    """

    accept_types = ()
    reject_types = ()
    type: str = None

    def __init__(self):
        self.extra_validators = []

    def validate(self, value):
        if value is None and self.nullable:
            return self.default

        if not isinstance(value, self.accept_types) or isinstance(
            value, self.reject_types
        ):
            raise ValidationError(
                f"Could not validate passed value `{value}` as a valid {self.type}."
            )
        for validator in self.extra_validators:
            value = validator.validate(value)

        return value
