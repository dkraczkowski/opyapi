from datetime import datetime
from datetime import timedelta
from datetime import timezone

import pytest

from opyapi.schema.formatters import format_datetime


@pytest.mark.parametrize(
    "input, expected_date",
    [
        ("2004-02-12T15:19:21", datetime(2004, 2, 12, 15, 19, 21)),
        (
            "2004-02-12T15:19:21+02:00",
            datetime(2004, 2, 12, 15, 19, 21, tzinfo=timezone(timedelta(hours=2))),
        ),
        (
            "2004-02-12T15:19:21Z",
            datetime(2004, 2, 12, 15, 19, 21, tzinfo=timezone.utc),
        ),
        (
            "2004-02-12T15:19:21-02:00",
            datetime(2004, 2, 12, 15, 19, 21, tzinfo=timezone(timedelta(hours=-2))),
        ),
        (
            "2004-02-12 15:19:21-02:00",
            datetime(2004, 2, 12, 15, 19, 21, tzinfo=timezone(timedelta(hours=-2))),
        ),
        (
            "20040212 151921-02:00",
            datetime(2004, 2, 12, 15, 19, 21, tzinfo=timezone(timedelta(hours=-2))),
        ),
    ],
)
def test_format_datetime(input, expected_date):

    formatted_value = format_datetime(input)
    assert isinstance(formatted_value, datetime)
    assert formatted_value == expected_date


@pytest.mark.parametrize("input", ["2010-10-41", "20102121"])
def test_fail_format_datetime(input):

    with pytest.raises(ValueError):
        format_datetime(input)
