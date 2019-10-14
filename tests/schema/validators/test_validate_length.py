import pytest

from opyapi.schema.errors import InvalidLengthError
from opyapi.schema.validators import validate_length


@pytest.mark.parametrize(
    "min_len,max_len,value",
    (
        (2, 10, "a" * 3),
        (1, 2, "a" * 2),
        (1, 2, "a"),
        (None, 3, "a" * 3),
        (2, None, "a" * 4),
    ),
)
def test_pass_validation(min_len, max_len, value):
    assert validate_length(value, minimum=min_len, maximum=max_len) is None


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, "a"), (1, 2, "a" * 3), (1, 2, ""), (None, 3, "a" * 4), (2, None, "a")),
)
def test_fail_validation(min_len, max_len, value):
    with pytest.raises(InvalidLengthError):
        assert validate_length(value, minimum=min_len, maximum=max_len)
