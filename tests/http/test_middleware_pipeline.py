import pytest

from opyapi.http import HttpRequest
from opyapi.http import HttpResponse
from opyapi.http import Middleware
from opyapi.http import MiddlewareHandler
from opyapi.http import MiddlewarePipeline


class ErrorCatchingMiddleware(Middleware):
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        try:
            assert isinstance(next, MiddlewareHandler)
            assert len(next.queue.queue) == 2
            response = next(request)
        except Exception as e:
            response = HttpResponse(500)
            response.body = e

        return response


class ProxingMiddleware(Middleware):
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        assert isinstance(next, MiddlewareHandler)
        assert len(next.queue.queue) == 1
        response = next(request)
        response.write(" Proxed Response")
        return response


class ErroringMiddleware(Middleware):
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        assert isinstance(next, MiddlewareHandler)
        assert len(next.queue.queue) == 0
        raise RuntimeError("Error")


class RespondingMiddleware(Middleware):
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        response = HttpResponse(201)
        response.write("Created")
        return response


def test_erroring_middleware_pipeline():
    pipeline = MiddlewarePipeline()
    pipeline.append(
        ErrorCatchingMiddleware(), ProxingMiddleware(), ErroringMiddleware()
    )

    response = pipeline(HttpRequest("get"))

    assert response.status_code == 500
    assert isinstance(response.body, RuntimeError)


def test_empty_pipeline():
    pipeline = MiddlewarePipeline()

    with pytest.raises(RuntimeError):
        pipeline(HttpRequest("get"))


def test_successing_pipeline():
    pipeline = MiddlewarePipeline()
    pipeline.append(
        ErrorCatchingMiddleware(), ProxingMiddleware(), RespondingMiddleware()
    )

    response = pipeline(HttpRequest("get"))
    response.body.seek(0)
    assert response.status_code == 201
    assert response.body.read() == b"Created Proxed Response"
