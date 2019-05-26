from __future__ import annotations
from abc import ABC, abstractmethod


class Schema(ABC):
    type: str = None
    default = None
    read_only: bool = False
    write_only: bool = False
    nullable: bool = None
    deprecated: bool = False
    description: str = ""

    @abstractmethod
    def to_doc(self):
        pass

    def _get_base_doc(self):
        doc = {"type": self.type}

        if self.nullable is not None:
            doc["nullable"] = self.nullable

        if self.default is not None:
            doc["default"] = self.default

        if self.deprecated:
            doc["deprecated"] = self.deprecated

        if self.description is not None:
            doc["description"] = self.description

        return doc
