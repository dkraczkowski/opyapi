import pytest
from opyapi.schema import validators
from opyapi.schema.errors import ValidationError


@pytest.mark.parametrize(
    "input",
    [
        "email@example.com",
        "email@subdomain.example.com",
        "firstname.lastname@example.com",
        "firstname+lastname@example.com",
        "email@123.123.123.123",
        "1234567890@example.com",
        "email@example-one.com",
        "_______@example.com",
        "email@example.name",
        "email@example.museum",
        "email@example.co.jp",
        "firstname-lastname@example.com",
    ],
)
def test_validate_valid_email_format(input: str):
    assert validators.validate_email(input) is None


@pytest.mark.parametrize(
    "input",
    [
        "plainaddress",
        "#@%^%#$@#$@#.com",
        "@example.com",
        "Joe Smith <email@example.com>",
        "email.example.com",
        "email@example@example.com",
        "email..email@example.com",
        "email@example.com (Joe Smith)",
        "email@-example.com",
        "email@example..com",
        "Abc..123@example.com",
    ],
)
def test_validate_invalid_email_format(input: str):
    with pytest.raises(ValidationError):
        validators.validate_email(input)
