from io import BytesIO
from typing import Optional

from .body import RequestBody
from ..query_string import parse_qs


class FormBody(RequestBody):
    @classmethod
    def from_wsgi(
        cls, wsgi_input: BytesIO, encoding: Optional[str] = None
    ) -> "FormBody":
        wsgi_input.seek(0)
        decoded_input = wsgi_input.read().decode(encoding)
        fields = parse_qs(decoded_input)
        instance = cls()

        for name, value in fields.items():
            instance[name] = value

        return instance


__all__ = [FormBody]
