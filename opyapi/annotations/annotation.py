from __future__ import annotations

_ANNOTATIONS = "__opyapi_annotations__"


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
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, [])
        target.__dict__[_ANNOTATIONS].append(self)
        return target
