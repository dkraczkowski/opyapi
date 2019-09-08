from opyapi.api import Operation
from opyapi.api import Response
from opyapi.api import TextContent
from opyapi.controller import resolve_arguments
from opyapi.http import HttpRequest
from opyapi.http import Route

fixture_route = Route("/resource/{id}/{sub_resource}").match("/resource/12/test")
fixture_request = HttpRequest("get")


def test_resolve_route_parameters():
    @Operation(
        path="/resource/{id}/{sub_resource}", responses=[Response(TextContent())]
    )
    def test_controller(id: int, sub_resource):
        return id, sub_resource

    args = resolve_arguments(test_controller, fixture_route, fixture_request)

    assert args == [12, "test"]


def test_resolve_request_parameter():
    @Operation(
        path="/resource/{id}/{sub_resource}", responses=[Response(TextContent())]
    )
    def test_controller(request: HttpRequest):
        return request

    args = resolve_arguments(test_controller, fixture_route, fixture_request)

    assert args == [fixture_request]
