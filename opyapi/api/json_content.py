from .media_type import MediaType
from .schema import Schema


class JsonContentType:
    def __getitem__(self, schema: Schema) -> MediaType:
        if schema is None:
            raise ValueError(
                "JsonContent requires subtype to be specified, None passed."
            )

        return MediaType("application/json", schema)


JsonContent = JsonContentType()


__all__ = ["JsonContent"]
