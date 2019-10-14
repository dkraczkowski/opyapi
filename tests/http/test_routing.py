import pytest

from opyapi.http.errors import NotFoundError
from opyapi.http.routing import Route
from opyapi.http.routing import Router


def test_route_parsing():
    route = Route("/example/{pattern}")
    assert route.match("/example/test")

    route = Route("/example/{pattern}", pattern=r"\d+")
    assert route.match("/example/12")
    assert not route.match("/example/fail")


def test_route_match():
    route = Route("/pets/{pet_id}")
    route = route.match("/pets/11a22")
    assert route["pet_id"] == "11a22"

    route = Route("/pets/{pet_id}", pet_id=r"\d+")
    assert not route.match("/pets/11a22")
    route = route.match("/pets/22")
    assert route._attributes == {"pet_id": "22"}


def test_router():
    def test_controller():
        pass

    router = Router()
    router.add_route("GET", Route("/pets/{pet_id}"), test_controller)
    router.add_route("get", Route("/pets"), test_controller)
    match = router.match("GET", "/pets/12")

    assert match[0]["pet_id"] == "12"
    assert router.match("get", "/pets")


def test_router_fail_matching():
    def test_controller():
        pass

    router = Router()
    router.add_route("GET", Route("/pets/{pet_id}"), test_controller)
    with pytest.raises(NotFoundError):
        router.match("POST", "/pets/12")


def test_route_match_multiple_parameters():
    route = Route("/pets/{pet_id}/{category}")
    route = route.match("/pets/11a22/test")
    assert route["pet_id"] == "11a22"
    assert route["category"] == "test"
