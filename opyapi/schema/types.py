from __future__ import annotations
import numbers
from .validators import Validator


class Type(Validator):
    """
    Reflects available types in the open api specification

    :: _Open Api types: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#data-types
    """

    accept_types = ()
    reject_types = ()
    name = "type"

    def __init__(self, accept_types: tuple = None, reject_types: tuple = None):
        if accept_types:
            self.accept_types = accept_types
        if reject_types:
            self.reject_types = reject_types

    def validate(self, value):
        if not isinstance(value, self.accept_types) or isinstance(
            value, self.reject_types
        ):
            raise self.error(value)
        return value


class Integer(Type):

    accept_types = int
    reject_types = bool
    name = "integer"


class Number(Type):

    accept_types = numbers.Number
    reject_types = bool
    name = "number"


class String(Type):

    accept_types = str
    reject_types = bool
    name = "string"


class Boolean(Type):

    accept_types = bool
    name = "boolean"


class Object(Type):

    accept_types = (object, dict)
    name = "object"


class Array(Type):

    accept_types = (tuple, list)
    name = "array"
