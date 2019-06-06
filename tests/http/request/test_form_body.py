from io import BytesIO
from opyapi.http import HttpRequest
from opyapi.http.request import FormBody
from opyapi.http.request import FormField

test_wsgi_body = {
    "CONTENT_TYPE": "application/x-www-form-urlencoded; charset=utf-8",
    "REQUEST_METHOD": "POST",
    "wsgi.input": BytesIO(b"test_1=1&test_2=Test+2&test_3=%7Btest+3%7D"),
}


def test_post_body():
    request = HttpRequest.from_wsgi(test_wsgi_body)
    body = request.parsed_body
    assert isinstance(body, FormBody)
    assert isinstance(body["test_1"], FormField)
    assert str(body["test_1"]) == "1"
    assert body.get("test2", "default") == "default"
