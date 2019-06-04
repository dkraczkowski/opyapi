from opyapi.http import Request


def test_can_instantiate():
    instance = Request("GET")
    assert isinstance(instance, Request)
