from .request_body import MultipartDataParser

class Request:
    def __init__(self, environ):
        self._environ = environ
        self._headers = {}
        self._normalized_headers = {}
        self._parsed_body = None
        self._build_headers()
        self._read_body()

    @property
    def headers(self):
        return self._headers

    def get_header(self, name: str):
        name = name.replace("-", "").replace("_", "").lower()
        return self._normalized_headers[name] if name in self._normalized_headers else None

    @property
    def body(self):
        return self._environ["wsgi.input"]

    @property
    def method(self):
        return self._environ["REQUEST_METHOD"]

    @property
    def query_string(self):
        return self._environ.get("QUERY_STRING", "")

    @property
    def path_info(self):
        return self._environ.get("PATH_INFO", "/")

    @property
    def parsed_body(self):
        return self._parsed_body

    def _build_headers(self):
        for key, value in self._environ.items():
            if not key.startswith("HTTP"):
                continue
            self._headers[key[5:]] = value
            self._normalized_headers[key[5:].replace("_", "").lower()] = value

    def _read_body(self):

        body_size = int(self._environ.get('CONTENT_LENGTH', 0))
        raw_body = self._environ['wsgi.input'].read(body_size)
        parser = MultipartDataParser(raw_body, "aaa")
        parser.parse()

        self._parsed_body = raw_body
