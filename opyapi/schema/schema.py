from __future__ import annotations
from . import Type
from . import Format


class Schema:
    def __init__(
        self,
        schema_type: Type,
        description: str = "",
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
        items: Schema = None,
        required: list = None,
    ):
        """
        :param schema_type:
        :param description:
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
        :param required:
        """
        self.description = description
        self.required = required
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

