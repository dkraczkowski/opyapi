from __future__ import annotations
from ..application import Application

_ANNOTATION = "__opyapi_annotation__"


class Annotation:
    """
    Base class for all other classes that are used as decorators,
    responsible for binding open annotations annotations into user-land classes.
    """

    def __call__(self, target):
        """
        :param target: annotated class or method
        :return: returns the target instance with applied annotations annotations
        """
        if not hasattr(target, _ANNOTATION):
            setattr(target, _ANNOTATION, None)
        target.__dict__[_ANNOTATION] = self
        Application.add_component(target)

        return target
