import pytest

from opyapi.api import Resource
from opyapi.schema import Schema
from opyapi.schema.types import *


@Resource(title="Example user fixture", required=("name",))
class UserFixture:
    name: Schema(String)


def test_resource_properties():
    a = UserFixture(name="Test User")
    b = a.name

    c = 1
