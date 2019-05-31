import re
import sys
from tempfile import TemporaryFile
from urllib.parse import parse_qs
from io import BytesIO
from enum import Enum


class State(Enum):
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
        state = State.PART_BOUNDARY
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

            if state is State.PART_BOUNDARY and line_break:
                if string_buffer == "--" + self._boundary:
                    string_buffer = ""
                    state = State.CONTENT_DISPOSITION
                else:
                    raise IOError("Could not parse request body, body is malformed or incorrect boundary was passed.")

            elif state is State.CONTENT_DISPOSITION and line_break:
                content_disposition = string_buffer
                string_buffer = ""
                state = State.CONTENT_TYPE
                if self._data[cursor + 1:cursor + 13].decode().lower() != "content-type":
                    state = State.CONTENT_HEADER
            elif state is State.CONTENT_TYPE and line_break:
                content_type = string_buffer
                state = State.CONTENT_HEADER
                string_buffer = ""
            elif state is State.CONTENT_HEADER and line_break:
                string_buffer = ""
                state = State.CONTENT_DATA
                content_cursor = cursor
            if state is State.CONTENT_DATA:
                if line_break and string_buffer == "--" + self._boundary:
                    content_data = self._data[content_cursor + 1: cursor - (len(self._boundary) + 5)]
                    parts.append({
                        "content_disposition": content_disposition,
                        "content_type": content_type,
                        "body": content_data,
                    })
                    content_type = None
                    state = State.CONTENT_DISPOSITION

                if line_break and string_buffer == "--" + self._boundary + "--":
                    content_data = self._data[content_cursor + 1: cursor - (len(self._boundary) + 7)]
                    parts.append({
                        "content_disposition": content_disposition,
                        "content_type": content_type,
                        "body": content_data,
                    })
                    content_type = None
                    state = State.END

                if line_break:
                    string_buffer = ""

            prev_byte = code
            cursor += 1

        return parts


class Part:
    pass


class MultipartBody:
    pass
