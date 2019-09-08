import io
import os
from importlib import util as reflection

import yaml
from cleo import Command

from opyapi import Application
from opyapi.api import OpenApi


class GenerateDocumentationCommand(Command):
    """
    Generates documentation from project directory

    build
        {input : filename of the entry point to your openapi project}
        {output? : documentation filename }
    """

    def handle(self):
        Application.suspend()
        self.add_style("error", fg="red", options=["bold"])
        self.add_style("success", fg="green", options=["bold"])

        input = self.argument("input")
        output = self.argument("output")

        self.line(f"Building project documentation for: `{input}`...")
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

        if not output:
            yaml.safe_dump(
                OpenApi.generate_doc(),
                self._io,
                default_flow_style=False,
                allow_unicode=True,
            )
            return 0
        if output[0] != "/":
            output = os.path.join(os.getcwd(), output)

        if not os.access(output, os.W_OK):
            self.line(
                "<error>Could not build project, output file is not writable.</error>"
            )
            return 1

        with io.open(output, "w") as output_stream:
            yaml.safe_dump(
                OpenApi.generate_doc(),
                output_stream,
                default_flow_style=False,
                allow_unicode=True,
            )

        return 0

    @staticmethod
    def load_module_from_file(module_file: str):
        spec = reflection.spec_from_file_location("api_project", module_file)
        module = reflection.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def read_project_dir(self, project_dir: str):
        pass
