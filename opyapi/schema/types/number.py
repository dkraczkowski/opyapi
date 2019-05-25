from __future__ import annotations
import numbers

from .type import Type


class Number(Type):

    accept_types = numbers.Number
    reject_types = bool
    name = "number"
    type = "number"
