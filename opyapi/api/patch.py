from typing import Dict
from typing import List

from .media_type import MediaType
from .operation import Operation


class Patch(Operation):
    def __init__(
        self, path: str, tags: List[str] = [], responses: Dict[int, MediaType] = {}
    ):
        super().__init__(path, "patch", tags, responses)


__all__ = ["Patch"]
