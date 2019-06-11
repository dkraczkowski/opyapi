from typing import Union

from .type import Type
from ..exceptions import ValidationError


class Object(Type):

    accept_types = (object, dict)
    type = "object"

    def __init__(
        self,
        properties: dict,
        title: str = "",
        description: str = "",
        required: Union[list, tuple] = (),
        nullable: bool = False,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        super().__init__()
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.nullable = nullable
        self.properties = properties
        self.required = required if required is not None else ()
        self.title = title
        self.description = description

    def validate(self, value: dict) -> dict:
        value = super().validate(value)
        for prop in self.required:
            if prop not in value:
                raise ValidationError(
                    f"Missing required property `{prop}` in passed dataset `{value}`"
                )

        for key, prop in self.properties.items():
            if key not in value:
                continue
            value[key] = prop.validate(value[key])

        return value

    def to_doc(self) -> dict:
        doc = self._get_base_doc()

        if self.required is not None:
            doc["required"] = self.required

        doc["properties"] = {}
        for key, prop in self.properties.items():
            doc["properties"][key] = prop.to_doc()

        return doc
