from __future__ import annotations


class Schema:
    type: str = None
    default = None
    read_only: bool = False
    write_only: bool = False
    nullable: bool = None
    deprecated: bool = False
    description: str = ""

    def to_doc(self):
        raise NotImplemented()

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

        if self.read_only is not None:
            doc["read_only"] = self.read_only

        if self.write_only is not None:
            doc["write_only"] = self.write_only

        return doc
