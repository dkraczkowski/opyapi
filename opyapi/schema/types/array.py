from __future__ import annotations

from .type import Type


class Array(Type):

    accept_types = (tuple, list)
    name = "array"
    type = "array"
