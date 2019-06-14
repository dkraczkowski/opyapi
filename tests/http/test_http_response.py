import pytest
from opyapi.http import HttpResponse, Headers


def test_can_instantiate():
    instance = HttpResponse(200)
    assert isinstance(instance, HttpResponse)


def test_can_write_and_read_body():
    instance = HttpResponse(200)
    instance.write("Example text")
    assert str(instance) == "Example text"
    instance.body.seek(0)
    assert instance.body.read() == b"Example text"


def test_headers():
    instance = HttpResponse()
    with pytest.raises(AttributeError):
        instance.headers = None

    assert isinstance(instance.headers, Headers)
