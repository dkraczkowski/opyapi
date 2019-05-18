from __future__ import annotations
from . import Annotation
from ..schema import Schema


class Resource(Annotation):
    """
    Resource replaces Open Api Schema Objects to simplify documentation process.

    .. _Open Api Schema: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#schemaObject
    """
    def __init__(self, title: str, description: str = "", schema: Schema = None):
        print("init")

    def __call__(self, target):
        print(target.__dict__["__annotations__"])
        print(target.__dict__["age"])
        return target
