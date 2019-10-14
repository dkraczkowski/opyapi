from datetime import datetime
from typing import Optional

from opyapi.schema.errors import NotWithinMaximumBoundaryError
from opyapi.schema.errors import NotWithinMinimumBoundaryError
from opyapi.schema.errors import ValidationError
from opyapi.schema.formatters import format_datetime


def validate_datetime(
    value: str, minimum: Optional[datetime] = None, maximum: Optional[datetime] = None
) -> None:
    try:
        datetime_value = format_datetime(value)
    except ValueError:
        raise ValidationError(f"Passed value {value} is not valid ISO 8601 datetime")

    if minimum and datetime_value < minimum:
        raise NotWithinMinimumBoundaryError(
            f"Passed date `{datetime_value}` is lower than set minimum value `{minimum}`."
        )

    if maximum and datetime_value > maximum:
        raise NotWithinMaximumBoundaryError(
            f"Passed date `{datetime_value}` is greater than set maximum value `{maximum}`."
        )


__all__ = ["validate_datetime"]
