from __future__ import annotations

from .type import Type


class Object(Type):

    accept_types = (object, dict)
    name = "object"
    type = "object"
