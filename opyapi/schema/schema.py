from __future__ import annotations
from .types import Type
import typing


class Schema:
    type: typing.Type[Type] = None
    format = None
    nullable: bool = False
    read_only: bool = False
    write_only: bool = False
    maximum: int = None
    minimum: int = None
    items: Schema = None
    min_items: int = None
    max_items: int = None
    unique_items: bool = False
    all_of: Schema = None
    one_of: tuple = ()
    pattern: str = None
    properties: dict = None
    enum: tuple = None
    required: tuple = ()
    default = None
    deprecated: bool = False
    title: str = ""
    description: str = ""

    def __init__(
        self,
        type: typing.Type[Type] = None,
        format=None,
        nullable: bool = False,
        read_only: bool = False,
        write_only: bool = False,
        maximum: int = None,
        minimum: int = None,
        items: Schema = None,
        min_items: int = None,
        max_items: int = None,
        unique_items: bool = False,
        all_of: Schema = None,
        one_of: tuple = None,
        pattern: str = None,
        properties: dict = None,
        enum: tuple = None,
        required: tuple = None,
        default=None,
        deprecated: bool = False,
        title: str = "",
        description: str = ""
    ):
        self.type = type
        self.format = format
        self.nullable = nullable
        self.read_only = read_only
        self.write_only = write_only
        self.maximum = maximum
        self.minimum = minimum
        self.items = items
        self.min_items = min_items
        self.max_items = max_items
        self.unique_items = unique_items
        self.all_of = all_of
        self.one_of = one_of
        self.pattern = pattern
        self.properties = properties
        self.enum = enum
        self.required = required
        self.default = default
        self.deprecated = deprecated
        self.title = title
        self.description = description
