from __future__ import annotations

from .type import Type


class Boolean(Type):

    accept_types = bool
    name = "boolean"
    type = "boolean"
