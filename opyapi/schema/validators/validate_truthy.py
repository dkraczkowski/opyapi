from typing import Any

from opyapi.schema.errors import ValidationError
from opyapi.schema.formatters import format_boolean


def validate_truthy(value: Any) -> None:
    try:
        formatted_value = format_boolean(value)
    except ValueError:
        raise ValidationError(f"Passed value {value} is not valid truthy expression.")

    if formatted_value is True:
        return

    raise ValidationError(f"Passed value {value} is not valid truthy expression.")


__all__ = ["validate_truthy"]
