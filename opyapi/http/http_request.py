from cgi import parse_header
from io import BytesIO
from .request.body import RequestBody
from .request.multipart_body import MultipartBody
from .request.form_body import FormBody
from .request.json_body import JsonBody
from .query_string import QueryString
from .headers import Headers


class HttpRequest:
    def __init__(
        self,
        method: str,
        path_info: str = "/",
        body: BytesIO = None,
        query_string: QueryString = None,
        headers: Headers = None,
    ):
        self.headers = headers if headers else Headers()
        self.body = body if body else BytesIO(b"")
        self.route = None
        self.method = method
        self.path = path_info
        self.query_string = query_string
        self._parsed_body = None
        self._parse_body()

    @property
    def parsed_body(self) -> RequestBody:
        return self._parsed_body

    def _parse_body(self) -> None:
        content_type = parse_header(self.headers.get("Content-Type", ""))

        if content_type[0] == "multipart/form-data":
            body = MultipartBody.from_wsgi(
                self.body,
                content_type[1].get("charset", ""),
                content_type[1].get("boundary"),
            )
        elif content_type[0] == "application/x-www-form-urlencoded":
            body = FormBody.from_wsgi(self.body, content_type[1].get("charset", ""))

        elif content_type[0] == "application/json":
            body = JsonBody.from_wsgi(self.body, content_type[1].get("charset", ""))
        else:
            self.body.seek(0)
            body = self.body.read().decode(content_type[1].get("charset", ""))

        self._parsed_body = body

    @classmethod
    def from_wsgi(cls, environ) -> "HttpRequest":
        headers = Headers()
        for key, value in environ.items():
            if not key.startswith("HTTP"):
                continue
            headers.add_header(key, value)
        headers.add_header("Content-Type", environ.get("CONTENT_TYPE", "text/plain"))
        return cls(
            method=environ.get("REQUEST_METHOD", "GET"),
            path_info=environ.get("PATH_INFO", "/"),
            body=environ.get("wsgi.input", BytesIO(b"")),
            query_string=QueryString(environ.get("QUERY_STRING", "")),
            headers=headers,
        )


__all__ = [HttpRequest]
