from typing import Any
from typing import Dict
from typing import Optional


class Schema:
    type: str
    default: Optional[Any] = None
    read_only: bool = False
    write_only: bool = False
    nullable: bool
    deprecated: bool = False
    description: str = ""

    def to_doc(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {"type": self.type}

        if self.nullable:
            result["nullable"] = self.nullable

        if self.default is not None:
            result["default"] = self.default

        if self.deprecated:
            result["deprecated"] = self.deprecated

        if self.description:
            result["description"] = self.description

        if self.read_only:
            result["readOnly"] = self.read_only

        if self.write_only:
            result["writeOnly"] = self.write_only

        return result


__all__ = ["Schema"]
