from __future__ import annotations
import json
from io import BytesIO
from .body import RequestBody


class JsonBody(RequestBody):
    def __init__(self, value: dict):
        self._body = value

    @classmethod
    def from_wsgi(cls, wsgi_input: BytesIO, encoding: str = None) -> JsonBody:
        wsgi_input.seek(0)
        decoded_input = wsgi_input.read().decode(encoding)

        instance = cls(json.loads(decoded_input))

        return instance


__all__ = [JsonBody]
