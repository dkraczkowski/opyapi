import json
from io import BytesIO
from json.decoder import JSONDecodeError
from typing import Optional

from .body import RequestBody


class JsonBody(RequestBody):
    def __init__(self, value: dict):
        self._body = value

    @classmethod
    def from_wsgi(
        cls, wsgi_input: BytesIO, encoding: Optional[str] = None
    ) -> "JsonBody":
        wsgi_input.seek(0)
        decoded_input = wsgi_input.read().decode(encoding)

        try:
            body = json.loads(decoded_input)
        except JSONDecodeError:
            body = {}

        instance = cls(body)

        return instance


__all__ = [JsonBody]
