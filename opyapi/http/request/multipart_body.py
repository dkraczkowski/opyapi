from __future__ import annotations
from cgi import parse_header
from enum import Enum
from io import BytesIO
from tempfile import TemporaryFile

from .form_body import FormBody, FormField


class ParserState(Enum):
    PART_BOUNDARY = 0
    CONTENT_DISPOSITION = 1
    CONTENT_TYPE = 2
    CONTENT_HEADER = 3
    CONTENT_DATA = 4
    END = 5


def _parse_multipart_data(data, boundary: str, encoding: str = None):
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

            field = FormFileField(
                _content_disposition[1]["name"],
                tmp_file,
                _content_type[14:].lower(),
                _content_disposition[1]["filename"]
            )
        else:
            field = FormField(_content_disposition[1]["name"], _content_data.decode(encoding))

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


class FormFileField(FormField):
    def __init__(self, name: str, value: TemporaryFile, mimetype: str, filename: str):
        super().__init__(name, value)
        self.mimetype = mimetype
        self.filename = filename
        self._str = None

    def read(self):
        return self.value.read()

    def seek(self, offset: int):
        return self.value.seek(offset)

    def close(self):
        return self.value.close()

    def save(self, path: str):
        if self.value.closed:
            raise ValueError(f"Cannot save to file {path} of closed stream.")
        with open(path, "wb") as file:
            self.seek(0)
            file.write(self.read())

        return file

    def __float__(self):
        raise ValueError(f"Cannot convert instance of {TemporaryFile.__name__} to float")

    def __int__(self):
        raise ValueError(f"Cannot convert instance of {TemporaryFile.__name__} to int")

    def __len__(self):
        return len(self.value)

    def __bool__(self):
        return len(self) > 0

    def __str__(self):

        if not self._str:
            self._str = self.read().decode()

        return self._str


class MultipartBody(FormBody):

    @staticmethod
    def from_wsgi(wsgi_input: BytesIO, encoding: str = None, boundary: str = None) -> MultipartBody:
        assert boundary, "%s.from_wsgi requires boundary parameter." % MultipartBody.__name__
        return _parse_multipart_data(wsgi_input.read(), boundary, encoding)
