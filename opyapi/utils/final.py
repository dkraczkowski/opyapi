class Final:
    """
    Mixin to prohibit from extending
    """

    def __init_subclass__(cls, *args, **kwargs):
        raise TypeError("Cannot subclass special typing classes")
