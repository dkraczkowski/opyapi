import pytest

from opyapi.schema.errors import ValidationError
from opyapi.schema.validators import validate_url


@pytest.mark.parametrize(
    "value",
    (
        "http://foo.com/blah_blah",
        "http://foo.com/blah_blah/",
        "https://www.example.com/foo/?bar=baz&inga=42&quux",
        "http://userid:password@example.com",
        "http://142.42.1.1:8080/",
        "http://142.42.1.1/",
        "http://code.google.com/events/#&product=browser",
        "http://a.b-c.de",
        "https://foo_bar.example.com/",
        "http://jabber.tcp.gmail.com",
        "http://_jabber._tcp.gmail.com",
        "http://مثال.إختبار",
    ),
)
def test_valid_values(value: str):
    assert validate_url(value) is None


@pytest.mark.parametrize(
    "value",
    (
        "http://",
        "http://.",
        "http://##/",
        "http://foo.bar?q=Spaces should be encoded",
        "http://-error-.invalid/",
        "http://0.0.0.0",
        "http://3628126748",
        "http://3628126748",
    ),
)
def test_invalid_values(value: str):
    with pytest.raises(ValidationError):
        validate_url(value)
