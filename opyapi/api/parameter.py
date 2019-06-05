from __future__ import annotations
from ..schema import Schema


class Parameter:
    def __init__(
        self,
        name: str,
        location: str,
        description: str = "",
        required: bool = False,
        schema: Schema = None,
        example=None,
        pattern: str = None,
    ):
        assert location in (
            "query",
            "header",
            "path",
            "cookie",
        ), f"Invalid location `{location}` passed for parameter"
        self.name = name
        self.location = location
        self.description = description
        self.required = required
        self.schema = schema
        self.example = example
        self.pattern = pattern
