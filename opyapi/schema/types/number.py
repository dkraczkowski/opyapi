from __future__ import annotations
import numbers

from .integer import Integer


class Number(Integer):

    accept_types = numbers.Number
    reject_types = bool
    type = "number"
