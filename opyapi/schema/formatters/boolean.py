from typing import Any


def format_boolean(value: Any) -> bool:
    if isinstance(value, str):
        value = value.lower()
    if value in (0, 0.0, "0", False, "no", "n", "nope", "false"):
        return False
    if value in (1, 1.0, "1", True, "ok", "yes", "y", "yup", "true"):
        return True

    raise ValueError("Passed value cannot be formatted to boolean.")
