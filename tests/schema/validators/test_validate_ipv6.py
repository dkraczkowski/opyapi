import pytest

from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate_ipv6


@pytest.mark.parametrize(
    "value",
    ("1200:0000:AB00:1234:0000:2552:7777:1313", "21DA:D3:0:2F3B:2AA:FF:FE28:9C5A"),
)
def test_valid_values(value: str):
    assert validate_ipv6(value) is None


@pytest.mark.parametrize(
    "value",
    ("1200::AB00:1234::2552:7777:1313", "1200:0000:AB00:1234:O000:2552:7777:1313"),
)
def test_invalid_values(value: str):
    with pytest.raises(ValidationError):
        validate_ipv6(value)
