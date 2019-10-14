from datetime import time
from typing import Optional

from opyapi.schema.errors import NotWithinMaximumBoundaryError
from opyapi.schema.errors import NotWithinMinimumBoundaryError
from opyapi.schema.errors import ValidationError
from opyapi.schema.formatters import format_time


def validate_time(
    value: str, minimum: Optional[time] = None, maximum: Optional[time] = None
) -> None:
    """
    Validates time in iso standard
    :: _ISO Standard: http://tools.ietf.org/html/rfc3339#section-5.6
    """
    try:
        parsed_time = format_time(value)
    except ValueError:
        raise ValidationError(f"Passed value {value} is not compatible ISO time")

    if minimum and parsed_time < minimum:
        raise NotWithinMinimumBoundaryError(
            f"Passed time {value} is not within minimum boundary {minimum}"
        )

    if maximum and parsed_time > maximum:
        raise NotWithinMaximumBoundaryError(
            f"Passed time {value} is not within maximum boundary {maximum}"
        )


__all__ = ["validate_time"]
