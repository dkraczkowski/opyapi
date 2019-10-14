from ..parameter import Parameter


class CookieType:
    def __getitem__(self, *args):
        if args[0] is None:
            raise ValueError("Cookie requires subtype to be specified, None passed.")
        return Parameter(args[0], location="query")


Cookie = CookieType()


__all__ = ["Cookie"]
