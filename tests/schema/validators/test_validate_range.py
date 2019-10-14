import pytest

from opyapi.schema.errors import OutOfRangeError
from opyapi.schema.validators import validate_range


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, 3), (1, 2, 2), (1, 2, 1), (None, 3, 3), (2, None, 4)),
)
def test_pass_validation(min_len, max_len, value):
    assert validate_range(value, minimum=min_len, maximum=max_len) is None


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, 1), (1, 2, 3), (1, 2, 0), (None, 3, 4), (2, None, 1)),
)
def test_fail_validation(min_len, max_len, value):
    with pytest.raises(OutOfRangeError):
        assert validate_range(value, minimum=min_len, maximum=max_len)
