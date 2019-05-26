import pytest
from opyapi.schema.validators import Range
from opyapi.schema.exceptions import InvalidRangeError


def test_can_instantiate():
    validator = Range()
    assert validator.validate(10)


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, 3), (1, 2, 2), (1, 2, 1), (None, 3, 3), (2, None, 4)),
)
def test_pass_validation(min_len, max_len, value):
    validator = Range(minimum=min_len, maximum=max_len)

    assert validator.validate(value)


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, 1), (1, 2, 3), (1, 2, 0), (None, 3, 4), (2, None, 1)),
)
def test_fail_validation(min_len, max_len, value):
    validator = Range(minimum=min_len, maximum=max_len)

    with pytest.raises(InvalidRangeError):
        assert validator.validate(value)
