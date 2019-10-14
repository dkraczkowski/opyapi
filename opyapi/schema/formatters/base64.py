import base64
import binascii


def format_base64(value: str) -> bytes:
    try:
        decoded_value = base64.b64decode(value)
    except binascii.Error:
        raise ValueError("Passed value is not valid base64 encoded string.")

    return decoded_value
