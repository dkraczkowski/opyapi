from __future__ import annotations
from io import BytesIO
from .body import RequestBody


class JsonBody(RequestBody):

    @classmethod
    def from_wsgi(cls, wsgi_input: BytesIO, encoding: str = None) -> JsonBody:
        decoded_input = wsgi_input.read().decode(encoding)

        instance = cls()


        return instance
