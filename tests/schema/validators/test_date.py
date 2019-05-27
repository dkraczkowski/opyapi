import pytest
from opyapi.schema.validators import Date
from datetime import date


def test_can_instantiate():
    validator = Date()
    assert validator.validate("2016-09-18")


@pytest.mark.parametrize("value", ("2016-09-18", "20160918"))
def test_valid_values(value: str):
    validator = Date()
    formatted_date = validator.validate(value)

    assert isinstance(formatted_date, date)
    assert formatted_date.year == 2016
    assert formatted_date.month == 9
    assert formatted_date.day == 18
