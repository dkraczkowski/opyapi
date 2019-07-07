from .type import Type


class Boolean(Type):

    accept_types = bool
    type = "boolean"

    def __init__(
        self,
        description: str = "",
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
        self.description = description

    def to_doc(self) -> dict:
        return self._get_base_doc()


__all__ = ["Boolean"]
