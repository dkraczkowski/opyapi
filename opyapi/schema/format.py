from __future__ import annotations
from enum import Enum


class Format(Enum):
    """
    Reflects base available formats in open api specification with additional flavoured formats to
    help with validation process.

    :: _Open Api Formats: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypeFormat
    """

    INT32 = "int32"
    INT64 = "int64"
    FLOAT = "float"
    DOUBLE = "double"
    BYTE = "byte"
    DATE = "date"
    DATE_TIME = "date-time"
    PASSWORD = "password"
    EMAIL = "email"
    ALPHA = "alpha"
    ALPHA_NUMERIC = "alpha-numeric"
    TRUTHY = "truthy"
    FALSY = "falsy"
    URI = "uri"
    URL = "url"
    UUID = "uuid"
    IP = "ip"
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    IBAN = "iban"
