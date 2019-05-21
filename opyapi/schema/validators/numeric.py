from fractions import Fraction
from decimal import Decimal
from ..validator import validator

_NUMERIC_TYPES = (int, float, complex, Decimal, Fraction)


@validator
def is_integer(value, minimum: int = None, maximum: int = None):
    if not isinstance(value, int):
        return False

    if minimum and value < minimum:
        return False

    if maximum and value > maximum:
        return False

    return True


@validator
def is_numeric(value, minimum: int = None, maximum: int = None):
    pass
