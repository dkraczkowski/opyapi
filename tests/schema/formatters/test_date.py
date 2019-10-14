from opyapi.schema.formatters import format_date
import pytest
from datetime import date


@pytest.mark.parametrize(
    "input, expected_date",
    [("2010-10-21", date(2010, 10, 21)), ("20101021", date(2010, 10, 21))],
)
def test_format_date(input, expected_date):

    formatted_value = format_date(input)
    assert isinstance(formatted_value, date)
    assert formatted_value == expected_date


@pytest.mark.parametrize("input", ["2010-10-41", "20102121"])
def test_fail_format_date(input):

    with pytest.raises(ValueError):
        format_date(input)
