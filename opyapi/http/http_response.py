from io import BytesIO

from .headers import Headers


class HttpResponse:
    def __init__(self, status_code: int = 200):
        self.headers = Headers()
        self.status_code = status_code
        self.body = BytesIO()

    def write(self, body: str) -> None:
        self.body.write(body)

    def __str__(self):
        pass


__all__ = [HttpResponse]
