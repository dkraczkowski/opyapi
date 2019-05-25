import pytest

from opyapi.annotations import Resource
from opyapi.schema import Schema
from opyapi.schema.types import *


@Resource(title="Wallet")
class UserWalletFixture:
    currency: Schema(String)
    amount: Schema(Number)


@Resource(title="Example user fixture", required=("name",))
class UserFixture:
    name: Schema(String, max_length=256)
    wallet: Schema(UserWalletFixture)


def test_resource_properties():
    a = UserFixture(name="Test User")
    b = a.name

    c = 1
