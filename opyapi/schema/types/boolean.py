from .type import Type


class Boolean(Type):
    accept_types = bool
    type = "boolean"

    def __init__(
        self,
        nullable: bool = False,
        default=None,
        deprecated: bool = False,
        read_only: bool = False,
        write_only: bool = False,
    ):
        self.write_only = write_only
        self.read_only = read_only
        self.deprecated = deprecated
        self.default = default
        self.nullable = nullable


__all__ = ["Boolean"]
