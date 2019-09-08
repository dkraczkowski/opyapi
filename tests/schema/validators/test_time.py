from datetime import time

import pytest

from opyapi.schema.validators import Time


def test_can_instantiate():
    validator = Time()
    assert validator.validate("17:34:02.124Z")


@pytest.mark.parametrize(
    "value", ("17:34:02.124Z", "17:34:02.124Z", "17:34:02", "17:34:02.124")
)
def test_valid_values(value: str):
    validator = Time()
    result = validator.validate(value)

    assert isinstance(result, time)
    assert result.hour == 17
    assert result.minute == 34
    assert result.second == 2
