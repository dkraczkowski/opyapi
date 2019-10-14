import pytest

from opyapi.schema.validators import validate_date


@pytest.mark.parametrize("value", [
    "2016-09-18",
    "20160918",
])
def test_valid_values(value: str):
    assert validate_date(value) is None

