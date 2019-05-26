import pytest
from opyapi.schema.types import Integer
from opyapi.schema.exceptions import ValidationError


def test_can_instantiate():
    test_integer = Integer()
    assert test_integer.validate(10)


@pytest.mark.parametrize("value", (None, "", "10", 12.3, False, True, 2j + 10))
def test_validation_fail(value):
    with pytest.raises(ValidationError):
        Integer().validate(value)


@pytest.mark.parametrize("value", (0, 1, -1, 200000000000000))
def test_validation_pass(value):
    assert Integer().validate(value) is value


@pytest.mark.parametrize("multiplication,value", ((2, 8), (3, 6), (1, 21), (-2, -8)))
def test_pass_multiple_of(multiplication, value):
    assert Integer(multiple_of=multiplication).validate(value) is value


@pytest.mark.parametrize("multiplication,value", ((2, 7), (3, 4), (-2, 9)))
def test_fail_multiple_of(multiplication, value):
    with pytest.raises(ValidationError):
        Integer(multiple_of=multiplication).validate(value)


@pytest.mark.parametrize(
    "min,max,value", ((2, 10, 8), (3, None, 6), (None, 21, 21), (-2, 0, -1))
)
def test_pass_range(min, max, value):
    assert Integer(minimum=min, maximum=max).validate(value) is value


@pytest.mark.parametrize(
    "min,max,value", ((2, 10, 1), (3, None, 2), (None, 21, 22), (-2, 0, 1))
)
def test_fail_range(min, max, value):
    with pytest.raises(ValidationError):
        Integer(minimum=min, maximum=max).validate(value)


def test_nullable():
    assert Integer(nullable=True).validate(None) is None


def test_doc_generation():
    schema = Integer(description="Test description", minimum=10)

    assert schema.to_doc() == {
        "description": "Test description",
        "minimum": 10,
        "nullable": False,
        "type": "integer",
    }
