from __future__ import annotations
import json
from json.decoder import JSONDecodeError
from io import BytesIO
from .body import RequestBody


class JsonBody(RequestBody):

    def __init__(self, value: dict):
        self._body = value

    @classmethod
    def from_wsgi(cls, wsgi_input: BytesIO, encoding: str = None) -> JsonBody:
        wsgi_input.seek(0)
        decoded_input = wsgi_input.read().decode(encoding)

        try:
            body = json.loads(decoded_input)
        except JSONDecodeError:
            body = {}

        instance = cls(body)

        return instance


__all__ = [
    JsonBody,
]
