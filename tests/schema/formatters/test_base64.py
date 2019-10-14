import base64

import pytest

from opyapi.schema.formatters import format_base64


def test_format_base64():
    encoded_string = base64.b64encode(b"test")
    value = format_base64(encoded_string)
    assert isinstance(value, bytes)
    assert value.decode("utf8") == "test"


def test_fail_format_base64():
    with pytest.raises(ValueError):
        format_base64("aaa")
