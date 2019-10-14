from ..parameter import Parameter


class PathType:
    def __getitem__(self, *args):
        if args[0] is None:
            raise ValueError("Path requires subtype to be specified, None passed.")
        return Parameter(args[0], location="path")


Path = PathType()


__all__ = ["Path"]
