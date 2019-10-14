from ..parameter import Parameter


class HeaderType:
    def __getitem__(self, *args):
        if args[0] is None:
            raise ValueError("Header requires subtype to be specified, None passed.")
        return Parameter(args[0], location="header")


Header = HeaderType()


__all__ = ["Header"]
