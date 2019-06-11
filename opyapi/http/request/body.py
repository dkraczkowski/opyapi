from typing import Any, Optional


class RequestBody:
    _body: dict = {}

    def get(self, name: str, default: Optional[Any] = None) -> Any:
        if name in self._body:
            return self._body[name]

        return default

    def __getitem__(self, name) -> Any:
        return self._body[name]

    def __contains__(self, name) -> Any:
        return name in self._body
