

class Schema:
    type: str = None
    default = None
    read_only: bool = False
    write_only: bool = False
    nullable: bool = None
    deprecated: bool = False
    description: str = ""

    def to_doc(self) -> dict:
        raise NotImplemented()

    def _get_base_doc(self) -> dict:
        doc = {"type": self.type}

        if self.nullable:
            doc["nullable"] = self.nullable

        if self.default is not None:
            doc["default"] = self.default

        if self.deprecated:
            doc["deprecated"] = self.deprecated

        if self.description:
            doc["description"] = self.description

        if self.read_only:
            doc["read_only"] = self.read_only

        if self.write_only:
            doc["write_only"] = self.write_only

        return doc
