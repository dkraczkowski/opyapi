from typing import Optional

from .base_error import OpyapiError
from ..http import HttpResponse


class HttpError(OpyapiError, HttpResponse):
    status_code: int = 500
    http_message = "Internal Server Error"

    def __init__(
        self, http_message: Optional[str] = None, status_code: Optional[int] = None
    ):
        HttpResponse.__init__(self, status_code if status_code else self.status_code)
        self.write(http_message if http_message else self.http_message)


class NotFoundError(HttpError):
    status_code: int = 404
    http_message = "Not Found"


__all__ = ["HttpError", "NotFoundError"]
