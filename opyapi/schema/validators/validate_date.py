from datetime import date
from typing import Optional
from typing import Union

from opyapi.schema.errors import NotWithinMaximumBoundaryError
from opyapi.schema.errors import NotWithinMinimumBoundaryError
from opyapi.schema.errors import ValidationError
from opyapi.schema.formatters import format_date


def validate_date(
    value: Union[str, date],
    minimum: Optional[date] = None,
    maximum: Optional[date] = None,
) -> None:
    try:
        date_value = format_date(value)
    except ValueError:
        raise ValidationError(f"Passed value {value} is not valid ISO 8601 date.")

    if not date_value:
        raise ValidationError(f"Passed value {value} is not valid ISO 8601 date.")

    if minimum and date_value < minimum:
        raise NotWithinMinimumBoundaryError(
            f"Passed date `{date_value}` is lower than set minimum value `{minimum}`."
        )

    if maximum and date_value > maximum:
        raise NotWithinMaximumBoundaryError(
            f"Passed date `{date_value}` is greater than set maximum value `{maximum}`."
        )


__all__ = ["validate_date"]
