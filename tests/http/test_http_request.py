from opyapi.http import HttpRequest


def test_can_instantiate():
    instance = HttpRequest("GET")
    assert isinstance(instance, HttpRequest)
