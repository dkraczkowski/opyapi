import io
import tempfile
from os import path

import pytest
import yaml
from cleo import Application
from cleo import CommandTester

from opyapi.opyapi import GenerateDocumentationCommand

OPYAPI_DIRNAME = path.abspath(path.join(path.dirname(__file__), "..", ".."))


def test_generate_from_file():
    application = Application()
    application.add(GenerateDocumentationCommand())

    test_unit = CommandTester(application.find("build"))
    api_path = path.join(OPYAPI_DIRNAME, "examples", "basic_api_example.py")
    _, output = tempfile.mkstemp()

    assert test_unit.execute(f"{api_path} {output}") == 0

    documentation = yaml.full_load(io.open(output, "r"))
    assert "info" in documentation
    assert documentation["info"]["title"] == "Pet shop API"
    assert documentation["info"]["version"] == "1.0.0"
    assert documentation["info"]["description"] == ""

    assert "servers" in documentation
    assert documentation["servers"][0]["url"] == "https://localhost:8080"
