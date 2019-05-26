from __future__ import annotations

from .type import Type


class Boolean(Type):

    accept_types = bool
    type = "boolean"

    def to_doc(self):
        return self._get_base_doc()
