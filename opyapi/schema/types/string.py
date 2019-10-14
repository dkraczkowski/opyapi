from enum import Enum
from typing import Any
from typing import Optional

from opyapi.schema import formatters
from opyapi.schema import validators
from .type import Type


class Format(Enum):
    DATETIME = "datetime"
    DATE = "date"
    TIME = "time"
    URI = "uri"
    URL = "url"
    EMAIL = "email"
    UUID = "uuid"
    HOSTNAME = "hostname"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    TRUTHY = "truthy"
    FALSY = "falsy"
    SEMVER = "semver"
    BYTE = "byte"


FORMAT_TO_VALIDATOR_MAP = {
    Format.DATETIME: validators.validate_datetime,
    Format.DATE: validators.validate_date,
    Format.TIME: validators.validate_time,
    Format.URI: validators.validate_uri,
    Format.URL: validators.validate_url,
    Format.EMAIL: validators.validate_email,
    Format.UUID: validators.validate_uuid,
    Format.HOSTNAME: validators.validate_hostname,
    Format.IPV4: validators.validate_ipv4,
    Format.IPV6: validators.validate_ipv6,
    Format.TRUTHY: validators.validate_truthy,
    Format.FALSY: validators.validate_falsy,
    Format.SEMVER: validators.validate_semver,
    Format.BYTE: validators.validate_base64,
}

FORMAT_TO_FORMATTER_MAP = {
    Format.DATETIME: formatters.format_datetime,
    Format.DATE: formatters.format_date,
    Format.TIME: formatters.format_time,
    Format.TRUTHY: formatters.format_boolean,
    Format.FALSY: formatters.format_boolean,
    Format.BYTE: formatters.format_base64,
}


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
        nullable: bool = False,
        default: Optional[str] = None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        self.nullable = nullable
        self.default = default
        self.deprecated = deprecated
        self.read_only = read_only
        self.write_only = write_only
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.format = string_format

    def validate(self, value: Any) -> None:
        super().validate(value)

        if self.min_length is not None or self.max_length is not None:
            validators.validate_length(value, self.min_length, maximum=self.max_length)

        if self.format in FORMAT_TO_VALIDATOR_MAP:
            validate_value = FORMAT_TO_VALIDATOR_MAP[self.format]
            validate_value(value)

    def format_value(self, value: Any) -> Any:
        if self.format in FORMAT_TO_FORMATTER_MAP:
            return FORMAT_TO_FORMATTER_MAP[self.format](value)

        return value


__all__ = ["String", "Format"]
