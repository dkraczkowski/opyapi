#!/usr/bin/env python
__version__ = "0.1.0"

from cleo import Application as Cli
from .http.routing import Route, Router
from .application import Application
from .opyapi import GenerateDocumentationCommand


def main():

    cli = Cli("opyapi", __version__, complete=False)
    cli.add(GenerateDocumentationCommand())
    cli.run()
