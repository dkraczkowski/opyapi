from io import BytesIO
from opyapi.http import Request
from opyapi.http.request import JsonBody

test_wsgi_body = {
    "CONTENT_TYPE": "application/json; charset=utf-8",
    "REQUEST_METHOD": "POST",
    "wsgi.input": BytesIO(b'{"test_1":"1","test_2":"Test 2","test_3":"{test 3}"}'),
}


def test_post_body():
    request = Request(test_wsgi_body)
    body = request.parsed_body
