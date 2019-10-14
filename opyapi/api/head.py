from typing import Dict
from typing import List

from .media_type import MediaType
from .operation import Operation


class Head(Operation):
    def __init__(
        self, path: str, tags: List[str] = [], responses: Dict[int, MediaType] = {}
    ):
        super().__init__(path, "head", tags, responses)


__all__ = ["Head"]
