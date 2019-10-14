from datetime import time
from datetime import timedelta
from datetime import timezone

import pytest

from opyapi.schema.formatters import format_time


@pytest.mark.parametrize(
    "input, expected_value",
    [
        ("15:19:21", time(15, 19, 21)),
        ("15:19:21+02:00", time(15, 19, 21, tzinfo=timezone(timedelta(hours=2)))),
        ("15:19:21Z", time(15, 19, 21, tzinfo=timezone.utc)),
        ("15:19:21-02:00", time(15, 19, 21, tzinfo=timezone(timedelta(hours=-2)))),
        ("151921-02:00", time(15, 19, 21, tzinfo=timezone(timedelta(hours=-2)))),
        (
            "151921.123-02:00",
            time(15, 19, 21, 123, tzinfo=timezone(timedelta(hours=-2))),
        ),
    ],
)
def test_format_datetime(input, expected_value):

    formatted_value = format_time(input)
    assert isinstance(formatted_value, time)
    assert formatted_value == expected_value


@pytest.mark.parametrize("input", ["2010-10-41", "20102121"])
def test_fail_format_datetime(input):

    with pytest.raises(ValueError):
        format_time(input)
