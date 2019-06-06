from .type import Type
from ..validators import (
    DateTime,
    Date,
    Time,
    Length,
    Uri,
    Url,
    Email,
    Uuid,
    Hostname,
    Ipv6,
    Ipv4,
    Truthy,
    Falsy,
)
from enum import Enum


class Format(Enum):
    DATETIME = DateTime()
    DATE = Date()
    TIME = Time()
    URI = Uri()
    URL = Url()
    EMAIL = Email()
    UUID = Uuid()
    HOSTNAME = Hostname()
    IPV4 = Ipv4()
    IPV6 = Ipv6()
    TRUTHY = Truthy()
    FALSY = Falsy()


class String(Type):

    accept_types = str
    reject_types = bool
    type = "string"

    def __init__(
        self,
        string_format: Format = None,
        min_length: int = None,
        max_length: int = None,
        pattern: str = None,
        description: str = "",
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = None,
        write_only: bool = None,
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
        doc = self._get_base_doc()

        if self.min_length is not None:
            doc["minLength"] = self.min_length

        if self.max_length is not None:
            doc["maxLength"] = self.max_length

        if self.pattern is not None:
            doc["pattern"] = self.pattern

        if self.format is not None:
            doc["format"] = self.format

        return doc
