import pytest

from opyapi.exceptions import InvalidLengthError
from opyapi.schema.validators import Length


def test_can_instantiate():
    validator = Length()
    assert validator.validate("a")


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
    validator = Length(minimum=min_len, maximum=max_len)

    assert validator.validate(value)


@pytest.mark.parametrize(
    "min_len,max_len,value",
    ((2, 10, "a"), (1, 2, "a" * 3), (1, 2, ""), (None, 3, "a" * 4), (2, None, "a")),
)
def test_fail_validation(min_len, max_len, value):
    validator = Length(minimum=min_len, maximum=max_len)

    with pytest.raises(InvalidLengthError):
        assert validator.validate(value)
