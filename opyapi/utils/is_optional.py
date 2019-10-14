from opyapi.schema.types.type import Type


def is_optional(type_definition) -> bool:
    if isinstance(type_definition, Type):
        return type_definition.nullable
    origin_type = getattr(type_definition, "__origin__", None)

    if origin_type and type(None) in type_definition.__args__:
        return True

    return False
