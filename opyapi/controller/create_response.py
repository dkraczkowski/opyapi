import json
from typing import Any
from typing import Callable
from typing import Dict

from ..api.annotation import read_annotation
from ..exceptions import HttpError
from ..http import HttpResponse
from ..schema import Object


def transform_object(obj: Any, mapping: dict, schema: Object) -> dict:
    result: Dict[str, Any] = {}
    for key, property in schema.properties.items():
        if key not in mapping:
            if property.nullable:
                result[key] = None
            else:
                raise ValueError(
                    f"Property `{key}` is not nullable, and must be defined in mapping scheme for {obj.__class__}"
                )
            continue

        mapped_key = mapping[key]
        if isinstance(mapped_key, str):
            result[key] = getattr(obj, mapped_key)
        elif mapped_key is True or mapped_key == 1:
            result[key] = getattr(obj, key)
        elif isinstance(mapped_key, Callable):
            result[key] = mapped_key(obj)
        else:
            raise ValueError(
                f"Property {key} has invalid mapping setting for object {obj.__class__}."
            )

    return result


def create_response(controller: Callable, args: list) -> HttpResponse:
    result = controller(*args)
    response_code = result[0]
    response_data = result[1]
    response_headers: Dict[str, str] = {}
    if len(result) == 3:
        response_headers = result[2]

    if isinstance(result, HttpResponse):
        return result

    if not isinstance(result, (list, tuple)):
        raise HttpError("Uri handler didnt return expected value", 406)

    annotation = read_annotation(controller)
    resource = None
    for response_annotation in annotation.responses:
        if response_annotation.status_code == result[0]:
            resource = response_annotation.schema
            break

    if not resource:
        raise HttpError("Uri handler could not return valid resource", 406)

    response = HttpResponse(response_code, headers=response_headers)
    if hasattr(response_data, "to_dict"):
        response.write(json.dumps(response_data.to_dict()))
    elif hasattr(response_data, "to_json"):
        response.write(response_data.to_json())
    else:
        response.write(
            json.dumps(
                transform_object(
                    response_data,
                    resource.mapping[response_data.__class__],
                    resource.schema,
                )
            )
        )

    return response


__all__ = ["create_response", "transform_object"]
