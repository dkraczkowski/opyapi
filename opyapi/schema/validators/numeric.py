from ..validator import validator


@validator()
def isinteger(value):
    return isinstance(value, int)


@validator()
def isnumeric(value):
    pass
