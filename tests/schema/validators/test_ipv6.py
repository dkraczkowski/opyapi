import pytest
from opyapi.schema.validators import Ipv6
from opyapi.schema.exceptions import ValidationError


def test_can_instantiate():
    validator = Ipv6()
    assert validator.validate("1200:0000:AB00:1234:0000:2552:7777:1313")


@pytest.mark.parametrize("value", (
    "1200:0000:AB00:1234:0000:2552:7777:1313",
    "21DA:D3:0:2F3B:2AA:FF:FE28:9C5A"
))
def test_valid_values(value: str):
    validator = Ipv6()
    assert validator.validate(value) == value


@pytest.mark.parametrize("value", (
    "1200::AB00:1234::2552:7777:1313",
    "1200:0000:AB00:1234:O000:2552:7777:1313"
))
def test_invalid_values(value: str):
    validator = Ipv6()
    with pytest.raises(ValidationError):
        assert validator.validate(value) == value
