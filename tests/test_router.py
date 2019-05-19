import pytest
from opyapi import parse_route


def test_parse_route():
    parse_route("/example/{pattern}")
