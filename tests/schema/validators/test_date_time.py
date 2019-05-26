import pytest
from opyapi.schema.validators import DateTime
from datetime import datetime


def test_can_instantiate():
    validator = DateTime()
    assert validator.validate("2016-09-18T17:34:02.124Z")


@pytest.mark.parametrize("value", (
    "2016-09-18T17:34:02.124Z",
    "2016-09-18 17:34:02.124Z",
    "2016-09-1817:34:02.124Z",
    "2016-09-1817:34:02Z",
    "2016-09-18T17:34:02+02:00",
    "20160918173402Z",
))
def test_valid_values(value: str):
    validator = DateTime()
    date = validator.validate(value)

    assert isinstance(date, datetime)
    assert date.year == 2016
    assert date.month == 9
    assert date.day == 18
    assert date.hour == 17
    assert date.minute == 34
    assert date.second == 2
