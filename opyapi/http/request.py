from enum import Enum
from cgi import parse_header
from tempfile import TemporaryFile


class ParserState(Enum):
    PART_BOUNDARY = 0
    CONTENT_DISPOSITION = 1
    CONTENT_TYPE = 2
    CONTENT_HEADER = 3
    CONTENT_DATA = 4
    END = 5


def parse_multipart_data(data, boundary: str, encoding: str = None):
    state = ParserState.PART_BOUNDARY
    prev_byte = None
    cursor = 0
    boundary_length = len(boundary)
    string_buffer = ""
    body = MultipartBody()

    def _append_content_to_body(_content_disposition: str, _content_type: str, _content_data):
        _content_disposition = parse_header(_content_disposition[20:])
        if "filename" in _content_disposition[1]:
            tmp_file = TemporaryFile()
            tmp_file.write(_content_data)
            tmp_file.seek(0)

            field = FileField(
                _content_disposition[1]["name"],
                tmp_file,
                _content_type[14:].lower(),
                _content_disposition[1]["filename"]
            )
        else:
            field = Field(_content_disposition[1]["name"], _content_data)

        body.append(field)

    content_disposition = ""
    content_type = None
    content_cursor = 0

    for code in data:
        line_break = code == 0x0a and prev_byte == 0x0d
        new_line_char = code == 0x0a or code == 0x0d

        if not new_line_char:
            string_buffer = string_buffer + chr(code)

        if state is ParserState.PART_BOUNDARY and line_break:
            if string_buffer == "--" + boundary:
                string_buffer = ""
                state = ParserState.CONTENT_DISPOSITION
            else:
                raise IOError("Could not parse request body, body is malformed or incorrect boundary was passed.")

        elif state is ParserState.CONTENT_DISPOSITION and line_break:
            content_disposition = string_buffer
            string_buffer = ""
            state = ParserState.CONTENT_TYPE
            if data[cursor + 1:cursor + 13].decode(encoding).lower() != "content-type":
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
            if line_break and string_buffer == "--" + boundary:
                content_data = data[content_cursor + 1: cursor - (boundary_length + 5)]
                _append_content_to_body(content_disposition, content_type, content_data)
                content_type = None
                state = ParserState.CONTENT_DISPOSITION

            if line_break and string_buffer == "--" + boundary + "--":
                content_data = data[content_cursor + 1: cursor - (boundary_length + 7)]
                _append_content_to_body(content_disposition, content_type, content_data)
                content_type = None
                state = ParserState.END

            if line_break:
                string_buffer = ""

        prev_byte = code
        cursor += 1

    return body


class QueryString:
    pass


class RequestBody:
    pass


class JsonBody(RequestBody):
    pass


class Field:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    def __int__(self):
        return int(self.content)

    def __str__(self):
        return str(self.content)

    def __float__(self):
        return float(self.content)

    def __bool__(self):
        return bool(self.content)

    def __len__(self):
        return len(self.content)


class FileField(Field):
    def __init__(self, name: str, content: TemporaryFile, mimetype: str, filename: str):
        self.name = name
        self.content = content
        self.mimetype = mimetype
        self.filename = filename
        self._str = None

    def read(self):
        return self.content.read()

    def seek(self, offset: int):
        return self.content.seek(offset)

    def close(self):
        return self.content.close()

    def save(self, path: str):
        if self.content.closed:
            raise ValueError(f"Cannot save to file {path} of closed stream.")
        file = open(path, "wb")
        self.seek(0)
        file.write(self.read())
        file.close()

        return file

    def __float__(self):
        raise ValueError(f"Cannot convert instance of {TemporaryFile.__name__} to float")

    def __int__(self):
        raise ValueError(f"Cannot convert instance of {TemporaryFile.__name__} to int")

    def __len__(self):
        return len(self.content)

    def __bool__(self):
        return len(self) > 0

    def __str__(self):

        if not self._str:
            self._str = self.read().decode()

        return self._str


class MultipartBody(RequestBody):
    def __init__(self):
        self._parts = {}

    def append(self, field: Field):
        if not isinstance(field, Field):
            raise ValueError(f"{MultipartBody.__name__}.append accepts only instance of {Field.__name__}")
        self._parts[field.name] = field

    def __getitem__(self, name):
        return self._parts[name]

    def __contains__(self, name):
        return name in self._parts


class PostBody(RequestBody):
    pass


class Headers:
    pass


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
        content_type = parse_header(self._environ.get('CONTENT_TYPE'))

        body = ""
        if content_type[0] == "multipart/form-data":
            body = parse_multipart_data(
                self._environ["wsgi.input"].read(body_size),
                content_type[1]["boundary"],
                content_type[1]["charset"]
            )

        self._parsed_body = body

