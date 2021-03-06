from io import BytesIO
from typing import Optional
from typing import Union

from .headers import Headers


class HttpResponse:
    def __init__(
        self,
        status_code: int = 200,
        encoding: str = "utf-8",
        headers: Optional[Union[dict, Headers]] = None,
    ):
        self._headers = headers if isinstance(headers, Headers) else Headers(headers)
        self.status_code = status_code
        self.body = BytesIO()
        self.encoding = encoding

    @property
    def headers(self):
        return self._headers

    def write(self, body: str) -> None:
        self.body.write(body.encode(self.encoding))

    @property
    def writable(self):
        return not self.body.closed

    def close(self):
        self.body.close()

    def __str__(self):
        self.body.seek(0)
        return self.body.read().decode(self.encoding)


__all__ = ["HttpResponse"]
