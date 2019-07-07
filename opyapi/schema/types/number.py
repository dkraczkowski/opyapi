import numbers

from .integer import Integer


class Number(Integer):

    accept_types = numbers.Number
    reject_types = bool
    type = "number"


__all__ = ["Number"]
