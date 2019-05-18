from __future__ import annotations
from . import Annotation


class Operation(Annotation):
    def __init__(self, method=None, route=None, responses=None, request=None):
        print("init")
