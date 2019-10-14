from typing import Any

from opyapi.schema.errors import ValidationError
from opyapi.schema.formatters import format_boolean


def validate_falsy(value: Any) -> None:
    try:
        formatted_value = format_boolean(value)
    except ValueError:
        raise ValidationError(f"Passed value {value} is not valid falsy expression.")

    if formatted_value is False:
        return

    raise ValidationError(f"Passed value {value} is not valid falsy expression.")


__all__ = ["validate_falsy"]
