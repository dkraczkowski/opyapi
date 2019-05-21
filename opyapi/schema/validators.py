from __future__ import annotations
from .exceptions import ValidationError


class _ValidatorMetaClass(type):
    def __new__(cls, name, bases, attrs):
        instance = type.__new__(cls, name, bases, attrs)

        return instance


class Validator(metaclass=_ValidatorMetaClass):

    name = None

    def validate(self, value):
        raise NotImplementedError

    def is_valid(self, value) -> bool:
        try:
            self.validate(value)
            return True
        except ValidationError:
            return False


class Type(Validator):

    accept_types = ()
    reject_types = ()

    def __init__(self, accept_types: tuple = None, reject_types: tuple = None):
        if accept_types:
            self.accept_types = accept_types
        if reject_types:
            self.reject_types = reject_types

    def validate(self, value):
        if not isinstance(value, self.accept_types) or isinstance(value, self.reject_types):
            raise ValidationError()
        return value


class Integer(Type):

    accept_types = int
    reject_types = bool
    name = "integer"

