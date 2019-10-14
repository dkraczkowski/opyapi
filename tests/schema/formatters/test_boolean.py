import pytest

from opyapi.schema.formatters import format_boolean


@pytest.mark.parametrize(
    "test_value,expected",
    [
        (1, True),
        (1.0, True),
        ("1", True),
        ("true", True),
        ("ok", True),
        ("yes", True),
        ("y", True),
        ("yup", True),
    ],
)
def test_format_true_boolean(test_value, expected):
    formatted_value = format_boolean(test_value)

    assert formatted_value == expected


@pytest.mark.parametrize(
    "test_value,expected",
    [
        (0, False),
        (0.0, False),
        ("0", False),
        ("false", False),
        ("no", False),
        ("nope", False),
        ("n", False),
    ],
)
def test_format_false_boolean(test_value, expected):
    formatted_value = format_boolean(test_value)

    assert formatted_value == expected


@pytest.mark.parametrize("test_value", ["invali", "a", "b", 2, "aye"])
def test_fail_format_boolean(test_value):
    with pytest.raises(ValueError):
        format_boolean(test_value)
