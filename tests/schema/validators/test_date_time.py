import pytest
from opyapi.schema.validators import DateTime


def test_can_instantiate():
    validator = DateTime()
    assert validator.validate("2016-09-18T17:34:02.124Z")
