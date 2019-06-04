from __future__ import annotations
from io import BytesIO

from .body import RequestBody
from ..query_string import parse_qs


class FormField:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return float(self.value)

    def __bool__(self):
        return bool(self.value)

    def __len__(self):
        return len(self.value)


class FormBody(RequestBody):
    def __init__(self):
        self._parts = {}

    def append(self, field: FormField):
        if not isinstance(field, FormField):
            raise ValueError(f"{FormBody.__name__}.append accepts only instance of {FormField.__name__}")
        self._parts[field.name] = field

    def __getitem__(self, name):
        return self._parts[name]

    def __contains__(self, name):
        return name in self._parts

    @classmethod
    def from_wsgi(cls, wsgi_input: BytesIO, encoding: str = None) -> FormBody:
        decoded_input = wsgi_input.read().decode(encoding)
        fields = parse_qs(decoded_input)
        instance = cls()

        for name, value in fields.items():
            instance.append(FormField(name, value))

        return instance
