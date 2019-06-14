from opyapi.api import Operation
from opyapi.http import Route, HttpRequest
from opyapi.controller import resolve_arguments


fixture_route = Route("/resource/{id}/{sub_resource}").match("/resource/12/test")
fixture_request = HttpRequest("get")


def test_resolve_route_parameters():
    @Operation(route="/resource/{id}/{sub_resource}")
    def test_controller(id: int, sub_resource):
        return id, sub_resource

    args = resolve_arguments(test_controller, fixture_route, fixture_request)

    assert args == [12, "test"]


def test_resolve_request_parameter():
    @Operation(route="/resource/{id}/{sub_resource}")
    def test_controller(request: HttpRequest):
        return request

    args = resolve_arguments(test_controller, fixture_route, fixture_request)

    assert args == [fixture_request]
