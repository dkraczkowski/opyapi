from __future__ import annotations
from .schema import Schema


def wrapper(cls, *args, **kwargs):
    print(cls.__dict__)


_ANNOTATIONS = "__opyapi_annotations__"


class Annotation:
    def __call__(self, target):
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, [])
        target.__dict__[_ANNOTATIONS].append(self)
        return target


class Api(Annotation):
    def __init__(self, title: str, servers: list = [], version: str = "1.0.0"):

        self.title = title
        self.servers = servers
        self.version = version


class Server(Annotation):
    def __init__(self, url, description: str = "", variables: list = []):
        print("init")


class Resource(Annotation):
    def __init__(self, title: str, description: str = "", schema: Schema = None):
        print("init")
