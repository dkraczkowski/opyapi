from __future__ import annotations
from enum import Enum


class Type(Enum):
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    OBJECT = "object"


class Format(Enum):
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


class Schema:
    def __init__(
        self,
        schema_type: Type = None,
        properties: dict = None,
        type_format: Format = None,
        deprecated: bool = False,
        nullable: bool = None,
        pattern: str = None,
        read_only: bool = False,
        write_only: bool = False,
        maximum: int = None,
        minimum: int = None,
        min_items: int = None,
        max_items: int = None,
        unique_items: bool = None,
        items: Schema = None
    ):
        """
        :param schema_type:
        :param properties:
        :param type_format:
        :param deprecated:
        :param nullable:
        :param pattern:
        :param read_only:
        :param write_only:
        :param maximum:
        :param minimum:
        :param min_items:
        :param max_items:
        :param unique_items:
        :param items:
        """
        self.items = items
        self.unique_items = unique_items
        self.max_items = max_items
        self.min_items = min_items
        self.minimum = minimum
        self.maximum = maximum
        self.write_only = write_only
        self.read_only = read_only
        self.pattern = pattern
        self.nullable = nullable
        self.type_format = type_format
        self.type = schema_type
        self.properties = properties
        self.format = format
        self.deprecated = deprecated


class Property:
    def __init__(self, property_type):
        pass
