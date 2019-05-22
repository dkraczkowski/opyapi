from __future__ import annotations
from . import Annotation
from ..schema import Schema


class Resource(Annotation, Schema):
    """
    Resource replaces Open Api Schema Objects to simplify documentation process.

    .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """

    def __init__(self, title: str, description: str = "", required: tuple = None, deprecated: bool = False):
        super().__init__(title=title, description=description, required=required, deprecated=deprecated)

    def __call__(self, target):
        self.properties = target.__dict__["__annotations__"]
        target.schema = self
        return target
