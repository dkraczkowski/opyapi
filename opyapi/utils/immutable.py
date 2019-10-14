class Immutable:
    """
    Mixin to indicate that object is immutable.
    """

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self
