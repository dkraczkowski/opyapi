import io
import os
from importlib import util as reflection

import yaml
from cleo import Command

from opyapi.api import Api


class GenerateDocumentationCommand(Command):
    """
    Generates documentation from project directory

    build
        {input : filename of the entry point to your openapi project}
        {output? : documentation filename }
    """

    def handle(self):
        self.add_style("error", fg="red", options=["bold"])
        self.add_style("success", fg="green", options=["bold"])
        input = self.argument("input")
        output = self.argument("output")

        if not os.path.isfile(input):
            self.line(
                "<error>Could not build project from given path."
                "You have to provide application's entry point to generate documentation.</error>"
            )
            return 1
        try:
            self.load_module_from_file(input)
        except Exception as e:
            self.line(
                "<error>Could not build project from given path. "
                f"There was an error loading your module: {e}</error>"
            )
            return 1

    @staticmethod
    def load_module_from_file(module_file: str):
        spec = reflection.spec_from_file_location("api_project", module_file)
        module = reflection.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def read_project_dir(self, project_dir: str):
        pass
