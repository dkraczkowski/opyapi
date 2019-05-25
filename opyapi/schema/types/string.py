from __future__ import annotations

from .type import Type


class String(Type):

    accept_types = str
    reject_types = bool
    name = "string"
    type = "string"
