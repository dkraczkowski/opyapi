from typing import Any, Optional
from collections import UserDict


class RequestBody(UserDict):
    def get(self, name: str, default: Optional[Any] = None) -> Any:
        if name in self:
            return self[name]

        return default
