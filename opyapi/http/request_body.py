import re
import sys
from tempfile import TemporaryFile
from urllib.parse import parse_qs
from io import BytesIO


class 


class MultipartDataParser:
    def __init__(self, binary_string, boundary: str):
        self._data = binary_string
        self._boundary = boundary

    def parse(self):

        prev_byte = None
        current_line = ""
        header = ""

        for code in self._data:
            line_break = code == 0x0a and prev_byte == 0x0d
            new_line_start = code == 0x0a or code == 0x0d

            if new_line_start:
                a = 2

            if line_break:
                b = 2

            if not new_line_start:
                current_line = current_line + chr(code)

            prev_byte = code

        return current_line
