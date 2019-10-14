from ..parameter import Parameter


class QueryType:
    def __getitem__(self, *args):
        if args[0] is None:
            raise ValueError("Query requires subtype to be specified, None passed.")
        return Parameter(args[0], location="query")


Query = QueryType()


__all__ = ["Query"]
