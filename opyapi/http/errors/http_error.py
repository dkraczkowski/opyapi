from typing import Optional

from opyapi import OpyapiError
from opyapi.http import HttpResponse


class HttpError(OpyapiError, HttpResponse):
    status_code: int = 500
    http_message = "Internal Server Error"

    def __init__(
        self, http_message: Optional[str] = None, status_code: Optional[int] = None
    ):
        HttpResponse.__init__(self, status_code if status_code else self.status_code)
        self.write(http_message if http_message else self.http_message)


__all__ = ["HttpError"]
