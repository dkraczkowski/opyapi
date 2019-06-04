from __future__ import annotations
from ..application import Application

_ANNOTATION_PROPERTY = "__opyapi_annotation__"


class Annotation:
    """
    Base class for all other classes that are used as decorators,
    responsible for binding open api api into user-land classes.
    """

    def __call__(self, target):
        """
        :param target: annotated class or method
        :return: returns the target instance with applied api api
        """
        setattr(target, _ANNOTATION_PROPERTY, self)
        return target
