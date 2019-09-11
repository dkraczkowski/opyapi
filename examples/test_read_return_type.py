from typing import Union


class GenericType:
    def __init__(self, origin, params, *, name=None):
        self.__origin__ = origin
        self.__params__ = params
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        result = self.__origin__(*args, **kwargs)
        return result


class Type:
    def __init__(self, name):
        self.__name__ = name

    def __getitem__(self, parameters):
        return GenericType(self, parameters)


class B:
    pass


A = Type("A")


def func_a(a: B) -> A[B]:
    pass


a = 1
