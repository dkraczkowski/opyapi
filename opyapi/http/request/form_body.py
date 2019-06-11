from io import BytesIO
from typing import Any, Optional

from .body import RequestBody
from ..query_string import parse_qs


class FormField:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __int__(self) -> int:
        return int(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __float__(self) -> float:
        return float(self.value)

    def __bool__(self) -> bool:
        return bool(self.value)

    def __len__(self) -> int:
        return len(self.value)


class FormBody(RequestBody):
    def __init__(self):
        self._body = {}

    def append(self, field: FormField) -> None:
        if not isinstance(field, FormField):
            raise ValueError(
                f"{FormBody.__name__}.append accepts only instance of {FormField.__name__}"
            )
        self._body[field.name] = field

    def get(self, name: str, default: Optional[Any] = None) -> Any:
        if name in self._body:
            return self._body[name].value

        return default

    @classmethod
    def from_wsgi(
        cls, wsgi_input: BytesIO, encoding: Optional[str] = None
    ) -> "FormBody":
        wsgi_input.seek(0)
        decoded_input = wsgi_input.read().decode(encoding)
        fields = parse_qs(decoded_input)
        instance = cls()

        for name, value in fields.items():
            instance.append(FormField(name, value))

        return instance


__all__ = [FormField, FormBody]
