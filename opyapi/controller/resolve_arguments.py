import inspect
from typing import Callable
from ..http import Route, HttpRequest
from ..http.message import FormBody, JsonBody, MultipartBody


def _resolve_to_resource(argument_type, argument_key, callback, request):
    try:
        if not argument_type.annotation:
            resource = callback.get_opyapi_annotation().request.schema
        else:
            resource = argument_type.annotation

        if not resource:
            raise ValueError(
                f"Callback {callback} defines parameter {argument_key} that cannot be resolved."
            )

        if not isinstance(
            request.parsed_body, (dict, FormBody, JsonBody, MultipartBody)
        ):
            raise ValueError(
                f"Request body cannot be resolved to {argument_key} parameter."
            )

        return resource(**request.parsed_body)

    except AttributeError:
        raise ValueError(
            f"Callback {callback} defines parameter {argument_key} that cannot be resolved."
        )


def _resolve_argument(
    argument_key: str,
    argument_type,
    callback: Callable,
    route: Route,
    request: HttpRequest,
):
    if argument_key in route:
        if argument_type.annotation in (int, float, str, bool):
            return argument_type.annotation(route[argument_key])
        else:
            return route[argument_key]
    elif argument_type.annotation is HttpRequest:
        return request
    elif argument_type.annotation is Route:
        return route
    else:
        return _resolve_to_resource(argument_type, argument_key, callback, request)


def resolve_arguments(callback: Callable, route: Route, request: HttpRequest) -> list:
    signature = inspect.signature(callback)
    args = []
    for argument_key, argument_type in signature.parameters.items():
        args.append(
            _resolve_argument(argument_key, argument_type, callback, route, request)
        )

    return args


__all__ = [resolve_arguments]
