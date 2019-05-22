from __future__ import annotations
from .exceptions import ValidationError


class Validator:

    name: str = None

    def validate(self, value):
        raise NotImplementedError

    def is_valid(self, value) -> bool:
        try:
            self.validate(value)
            return True
        except ValidationError:
            return False

    def error(self, value):
        return ValidationError(
            f"Could not validate passed value `{value}` as a valid {self.name}."
        )


class Range(Validator):

    minimum = None
    maximum = None
    name: str = "range"

    def __init__(self, minimum=None, maximum=None):
        if minimum:
            self.minimum = minimum

        if maximum:
            self.maximum = maximum

    def validate(self, value):
        if self.minimum and value < self.minimum:
            raise ValidationError(
                f"Passed value `{value}` is lower than set minimum value `{self.minimum}`."
            )

        if self.maximum and value > self.maximum:
            raise ValidationError(
                f"Passed value `{value}` is greater than set maximum value `{self.maximum}`."
            )

        return True


class Capacity(Validator):

    minimum_items: int = None
    maximum_items: int = None
    name: str = "capacity"

    def __init__(self, minimum=None, maximum=None):
        if minimum:
            self.minimum_items = minimum

        if maximum:
            self.maximum_items = maximum

    def validate(self, value):
        length = len(value)

        if self.minimum_items and length < self.minimum_items:
            raise ValidationError(
                f"Passed collection cannot be empty and must contain at least `{self.minimum_items}` items."
            )

        if self.maximum_items and length < self.maximum_items:
            raise ValidationError(
                f"Passed collection cannot contain more than `{self.maximum_items}` items."
            )


class OneOf(Validator):

    def __init__(self, *schemas):
        pass

    def validate(self, value):
        pass
