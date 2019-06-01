from enum import Enum
import re
from cgi import parse_header

_CONTENT_TYPE_REGEX = re.compile(r"([^\;]+)(\;([\w\s]+)\=([^\;]+))*", re.I)


class ParserState(Enum):
    PART_BOUNDARY = 0
    CONTENT_DISPOSITION = 1
    CONTENT_TYPE = 2
    CONTENT_HEADER = 3
    CONTENT_DATA = 4
    END = 5


class MultipartDataParser:
    def __init__(self, binary_string, boundary: str):
        self._data = binary_string
        self._boundary = boundary

    def parse(self):
        state = ParserState.PART_BOUNDARY
        prev_byte = None
        string_buffer = ""
        content_disposition = ""
        content_type = None
        content_cursor = 0
        cursor = 0
        parts = []

        for code in self._data:
            line_break = code == 0x0a and prev_byte == 0x0d
            new_line_char = code == 0x0a or code == 0x0d

            if not new_line_char:
                string_buffer = string_buffer + chr(code)

            if state is ParserState.PART_BOUNDARY and line_break:
                if string_buffer == "--" + self._boundary:
                    string_buffer = ""
                    state = ParserState.CONTENT_DISPOSITION
                else:
                    raise IOError("Could not parse request body, body is malformed or incorrect boundary was passed.")

            elif state is ParserState.CONTENT_DISPOSITION and line_break:
                content_disposition = string_buffer
                string_buffer = ""
                state = ParserState.CONTENT_TYPE
                if self._data[cursor + 1:cursor + 13].decode().lower() != "content-type":
                    state = ParserState.CONTENT_HEADER
            elif state is ParserState.CONTENT_TYPE and line_break:
                content_type = string_buffer
                state = ParserState.CONTENT_HEADER
                string_buffer = ""
            elif state is ParserState.CONTENT_HEADER and line_break:
                string_buffer = ""
                state = ParserState.CONTENT_DATA
                content_cursor = cursor
            if state is ParserState.CONTENT_DATA:
                if line_break and string_buffer == "--" + self._boundary:
                    content_data = self._data[content_cursor + 1: cursor - (len(self._boundary) + 5)]
                    parts.append({
                        "content_disposition": ContentType(content_disposition),
                        "content_type": content_type,
                        "body": content_data,
                    })
                    content_type = None
                    state = ParserState.CONTENT_DISPOSITION

                if line_break and string_buffer == "--" + self._boundary + "--":
                    content_data = self._data[content_cursor + 1: cursor - (len(self._boundary) + 7)]
                    parts.append({
                        "content_disposition": ContentType(content_disposition),
                        "content_type": content_type,
                        "body": content_data,
                    })
                    content_type = None
                    state = ParserState.END

                if line_break:
                    string_buffer = ""

            prev_byte = code
            cursor += 1

        return parts


class QueryString:
    pass


class RequestBody:
    pass


class JsonBody(RequestBody):
    pass


class MultipartBody(RequestBody):
    pass


class PostBody(RequestBody):
    pass


class Headers:
    pass


class MimeHeader:
    def __init__(self, string: str):
        self._raw = string
        info = parse_header(string[20:])
        self.content_type
        if self._raw:
            self._parse()

    def _parse(self):
        parse_header()
        match = _CONTENT_TYPE_REGEX.fullmatch(self._raw)
        a = 1

    @property
    def type(self):
        pass

    def __str__(self):
        return self._raw


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
        parser = MultipartDataParser(raw_body, "__X_PAW_BOUNDARY__")
        parser.parse()

        self._parsed_body = raw_body

