from .type import Type
from ..exceptions import ValidationError


class Object(Type):

    accept_types = (object, dict)
    type = "object"

    def __init__(
        self,
        properties: dict,
        title: str = None,
        description: str = None,
        required: list = None,
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = None,
        write_only: bool = None,
    ):
        super().__init__()
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
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
