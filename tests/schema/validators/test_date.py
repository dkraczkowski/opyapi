import pytest
from opyapi.schema.validators import Date
from datetime import datetime


def test_can_instantiate():
    validator = Date()
    assert validator.validate("2016-09-18")


@pytest.mark.parametrize("value", ("2016-09-18", "20160918"))
def test_valid_values(value: str):
    validator = Date()
    date = validator.validate(value)

    assert isinstance(date, datetime)
    assert date.year == 2016
    assert date.month == 9
    assert date.day == 18
