from abc import abstractmethod

ANNOTATION_PROPERTY = "__opyapi__"


class Annotation:
    """
    Base class for all other classes that are used as decorators,
    responsible for binding open api api into user-land classes.
    """

    @abstractmethod
    def __call__(self, target):
        pass


def bind_annotation(obj: object, annotation: Annotation) -> None:
    setattr(obj, ANNOTATION_PROPERTY, annotation)


def read_annotation(obj: object) -> Annotation:
    annotation = getattr(obj, ANNOTATION_PROPERTY, None)
    if annotation is None:
        raise ValueError(f"Could not read annotation data from object {obj}")
    return annotation


__all__ = ["Annotation", "bind_annotation", "read_annotation"]
