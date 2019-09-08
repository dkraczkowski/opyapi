from enum import Enum
from typing import Optional

from ..validators import Length
from ..validators import validators
from .type import Type


class Format(Enum):
    DATETIME = validators.date_time
    DATE = validators.date
    TIME = validators.time
    URI = validators.uri
    URL = validators.url
    EMAIL = validators.email
    UUID = validators.uuid
    HOSTNAME = validators.hostname
    IPV4 = validators.ipv4
    IPV6 = validators.ipv6
    TRUTHY = validators.truthy
    FALSY = validators.falsy
    SEM_VER = validators.sem_ver


class String(Type):

    accept_types = str
    reject_types = bool
    type = "string"

    def __init__(
        self,
        string_format: Optional[Format] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        description: str = "",
        nullable: bool = False,
        default: Optional[str] = None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        super().__init__()
        self.description = description
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated
        self.read_only = read_only
        self.write_only = write_only
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.format = string_format

        if min_length is not None or max_length is not None:
            self.extra_validators.append(Length(minimum=min_length, maximum=max_length))

        if string_format is not None and string_format in Format:
            self.extra_validators.append(string_format.value)

    def to_doc(self) -> dict:
        doc = super().to_doc()

        if self.min_length is not None:
            doc["minLength"] = self.min_length

        if self.max_length is not None:
            doc["maxLength"] = self.max_length

        if self.pattern is not None:
            doc["pattern"] = self.pattern

        if self.format is not None:
            doc["format"] = self.format

        return doc


__all__ = ["String", "Format"]
