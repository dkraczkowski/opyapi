import json
from typing import Any
from typing import Callable
from typing import Dict

from ..api.annotation import read_annotation
from ..exceptions import HttpError
from ..http import HttpResponse


def create_response(controller: Callable, args: list) -> HttpResponse:
    result: Any = controller(*args)

    if isinstance(result, HttpResponse):
        return result

    response_code: int = 406
    response_body: Any = "Uri handler didnt return expected value"
    response_headers: Dict[str, str] = {}

    if isinstance(result, (list, tuple)):
        if (
            len(result) < 2
            or not isinstance(result[0], int)
            or result[0] < 100
            or result[0] > 600
        ):
            raise HttpError(response_body, response_code)

        response_code = result[0]
        response_body = result[1]

        if len(result) >= 3:
            response_headers = result[2]
    else:
        response_code = 200
        response_body = result

    annotation = read_annotation(controller)
    resource = None
    for response_annotation in annotation.responses:
        if response_annotation.status_code == response_code:
            resource = response_annotation.content.schema
            break

    if not resource:
        raise HttpError("Uri handler could not return valid resource", 406)

    response = HttpResponse(response_code, headers=response_headers)
    if hasattr(response_body, "to_dict"):
        response.write(json.dumps(response_body.to_dict()))
    elif hasattr(response_body, "to_json"):
        response.write(response_body.to_json())
    else:
        """response.write(
            json.dumps(
                transform_object(
                    response_body,
                    resource.mapping[response_body.__class__],
                    resource.schema,
                )
            )
        )
        """
        pass

    return response


__all__ = ["create_response"]
