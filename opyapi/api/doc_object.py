from typing import Any
from typing import Dict


class DocObject:
    def to_doc(self) -> Dict[str, Any]:
        raise NotImplemented()


__all__ = ["DocObject"]
