from typing import Type, TypeVar

T = TypeVar("T")
_ANNOTATION_PROPERTY = "__opyapi_annotation__"


class Annotation:
    """
    Base class for all other classes that are used as decorators,
    responsible for binding open api api into user-land classes.
    """

    def __call__(self, target: Type[T]) -> T:
        """
        :param target: annotated class or method
        :return: returns the target instance with applied api api
        """
        setattr(target, _ANNOTATION_PROPERTY, self)

        def get_annotation():
            return getattr(target, _ANNOTATION_PROPERTY)

        target.get_opyapi_annotation = get_annotation

        return target


__all__ = [Annotation]
