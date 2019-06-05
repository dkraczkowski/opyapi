import pytest
from opyapi.schema.types import *
from opyapi.schema.exceptions import ValidationError


def test_can_instantiate():
    test_instance = Object({"test_property": String()})
    assert test_instance.validate({}) == {}


def test_validate_required_properties():
    test_instance = Object({"name": String(), "age": Integer()}, required=["name"])

    with pytest.raises(ValidationError):
        test_instance.validate({"age": 10})
